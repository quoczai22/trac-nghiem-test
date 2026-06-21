// Local Ollama helper cho admin/import-export.html
// Chạy local, không deploy lên GitHub Pages.
// Nhiệm vụ: nhận danh sách câu hỏi thiếu đáp án, gọi Ollama, trả về JSON gợi ý.

const http = require("http");

const PORT = Number(process.env.PORT || 3100);
const OLLAMA_URL = process.env.OLLAMA_URL || "http://localhost:11434";
const DEFAULT_MODEL = process.env.OLLAMA_MODEL || "qwen2.5:7b";

function sendJson(res, status, payload) {
  res.writeHead(status, {
    "Content-Type": "application/json; charset=utf-8",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
  });
  res.end(JSON.stringify(payload));
}

function readBody(req) {
  return new Promise((resolve, reject) => {
    let body = "";
    req.on("data", (chunk) => {
      body += chunk;
      if (body.length > 5 * 1024 * 1024) {
        reject(new Error("Payload quá lớn."));
        req.destroy();
      }
    });
    req.on("end", () => resolve(body ? JSON.parse(body) : {}));
    req.on("error", reject);
  });
}

function strictJsonFromText(text) {
  try {
    return JSON.parse(text);
  } catch {}
  const match = String(text || "").match(/\{[\s\S]*\}/);
  if (!match) throw new Error("Model không trả JSON.");
  return JSON.parse(match[0]);
}

async function askOllama(question, model) {
  const prompt = `You are solving a multiple-choice English/course question for import into a quiz bank.
Return ONLY valid JSON. No markdown.
Schema:
{"answer":"A|B|C|D|null","confidence":0.0-1.0,"explanation":"short Vietnamese explanation"}

Question:
${question.question}
A. ${question.options?.A || ""}
B. ${question.options?.B || ""}
C. ${question.options?.C || ""}
D. ${question.options?.D || ""}

Rules:
- Choose the best answer.
- If the question is ambiguous or requires a passage not provided, return answer null and confidence <= 0.5.
- For grammar/vocabulary, solve directly.
- Keep explanation under 25 Vietnamese words.`;

  const response = await fetch(`${OLLAMA_URL}/api/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      model,
      stream: false,
      messages: [
        { role: "system", content: "You are a strict JSON API for multiple-choice answer extraction." },
        { role: "user", content: prompt },
      ],
      options: {
        temperature: 0.1,
        top_p: 0.2,
      },
    }),
  });

  if (!response.ok) {
    const text = await response.text();
    throw new Error(`Ollama lỗi ${response.status}: ${text.slice(0, 200)}`);
  }

  const payload = await response.json();
  const content = payload.message?.content || "";
  const parsed = strictJsonFromText(content);
  const answer = String(parsed.answer || "").toUpperCase();

  return {
    index: question.index,
    answer: ["A", "B", "C", "D"].includes(answer) ? answer : null,
    confidence: Number(parsed.confidence || 0),
    explanation: String(parsed.explanation || ""),
  };
}

const server = http.createServer(async (req, res) => {
  if (req.method === "OPTIONS") return sendJson(res, 200, { ok: true });

  if (req.method === "GET" && req.url === "/") {
    return sendJson(res, 200, {
      ok: true,
      message: "Ollama helper is running.",
      ollamaUrl: OLLAMA_URL,
      defaultModel: DEFAULT_MODEL,
    });
  }

  if (req.method === "POST" && req.url === "/api/ai/resolve-answers") {
    try {
      const body = await readBody(req);
      const model = body.model || DEFAULT_MODEL;
      const questions = Array.isArray(body.questions) ? body.questions : [];
      if (!questions.length) return sendJson(res, 400, { message: "Thiếu questions." });

      const results = [];
      for (const question of questions) {
        try {
          results.push(await askOllama(question, model));
        } catch (error) {
          results.push({ index: question.index, answer: null, confidence: 0, explanation: error.message });
        }
      }

      return sendJson(res, 200, { results });
    } catch (error) {
      return sendJson(res, 500, { message: error.message });
    }
  }

  sendJson(res, 404, { message: "Not found" });
});

server.listen(PORT, () => {
  console.log(`Ollama helper running: http://localhost:${PORT}`);
  console.log(`Ollama API: ${OLLAMA_URL}`);
  console.log(`Default model: ${DEFAULT_MODEL}`);
});
