const express = require('express');
const cors = require('cors');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3200;

// Middleware
app.use(cors());
app.use(express.json({ limit: '50mb' }));
app.use(express.urlencoded({ limit: '50mb', extended: true }));

// Health check
app.get('/', (req, res) => {
  res.json({
    ok: true,
    message: 'AI Import service is running',
    version: '1.0.0'
  });
});

// Import questions endpoint
app.post('/api/import/questions', (req, res) => {
  try {
    const { questions, format } = req.body;
    
    if (!Array.isArray(questions)) {
      return res.status(400).json({ error: 'questions must be an array' });
    }

    // Process questions
    const processed = questions.map((q, idx) => ({
      index: idx,
      question: q.question || '',
      options: q.options || {},
      format: format || 'multiple-choice'
    }));

    res.json({
      ok: true,
      count: processed.length,
      questions: processed
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Batch import endpoint
app.post('/api/import/batch', (req, res) => {
  try {
    const { file, format } = req.body;
    
    if (!file) {
      return res.status(400).json({ error: 'file content required' });
    }

    res.json({
      ok: true,
      message: 'Batch import received',
      fileSize: file.length,
      format: format || 'unknown'
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Internal server error' });
});

// Start server
app.listen(PORT, () => {
  console.log(`AI Import service running on http://localhost:${PORT}`);
  console.log(`Environment: ${process.env.NODE_ENV || 'development'}`);
});
