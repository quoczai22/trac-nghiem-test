# AI Import Service

AI-powered question import tool for the quiz system.

## Installation

```bash
npm install
```

## Running

Development mode (with auto-reload):
```bash
npm run dev
```

Production mode:
```bash
npm start
```

## API Endpoints

### Health Check
```
GET /
```

### Import Questions
```
POST /api/import/questions
Content-Type: application/json

{
  "questions": [
    {
      "question": "What is 2+2?",
      "options": {
        "A": "3",
        "B": "4",
        "C": "5",
        "D": "6"
      }
    }
  ],
  "format": "multiple-choice"
}
```

### Batch Import
```
POST /api/import/batch
Content-Type: application/json

{
  "file": "<file content>",
  "format": "csv|json|xlsx"
}
```

## Port

Server runs on port 3200 (configurable via PORT env var)
