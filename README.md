# Smart SCM — Agentic AI Integrated Supply Chain Management

A beginner-friendly full-stack demo for textile supply-chain monitoring. It includes a React + Vite dashboard, a FastAPI backend, a local SQLite database, and rule-based agent logic for stock/demand/supplier risk recommendations. The default `AI_PROVIDER=demo` works without an API key.

## What the project does
1. **Inventory/Demand agent:** estimates days of stock and projected demand for the next 7 days.
2. **Supplier evaluation:** ranks suppliers using reliability, lead time, and price.
3. **Risk/procurement agent:** flags stock below reorder level and recommends a purchase quantity.
4. **Decision assistant:** returns suggested actions. A real purchase is not placed; a human must approve it.

> Note: The supplied React screen is currently a static sample dashboard with example numbers. The backend API uses seeded demo data and computes its own results. Connecting the screen to live API responses would be a separate enhancement. Treat all supplied data as demonstration data, not real business data.

## Requirements (Windows)
- Python 3.11 or newer
- Node.js 20 or newer (npm is included)

## Run it (no API key needed)
1. Extract the ZIP to a normal folder, e.g. `C:\Projects\smart-scm-agentic-ai-main`.
2. Open that folder in File Explorer.
3. In the folder address bar, type `cmd` and press Enter.
4. Run these commands one by one:

```bat
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r backend\requirements.txt
copy .env.example .env
```

5. Keep the first Command Prompt open and run the backend:

```bat
cd backend
python -m uvicorn app.main:app --reload --port 8000
```

6. Open a **second** Command Prompt in the project folder (repeat step 3). Run the frontend:

```bat
cd frontend
npm install
npm run dev
```

7. Open the local URL shown by Vite, usually `http://127.0.0.1:8000:5173`.
8. To inspect and test the backend, open `http://127.0.0.1:8000/docs`. Try `POST /api/ai/analyze`, then click **Try it out** and **Execute**. Also try `GET /api/dashboard` and `GET /api/inventory`.

## AI configuration
The demo runs with no key. To use an OpenAI-compatible API, set `AI_PROVIDER=openai`, `OPENAI_API_KEY`, and `OPENAI_MODEL` in `.env`. Do not share your API key or commit `.env` to Git.

## Main API endpoints
- `GET /api/health` — backend status
- `POST /api/seed` — initialize demo data if the database is empty
- `GET /api/dashboard` — summary, inventory risks and recommended actions
- `GET /api/inventory` — stock details
- `GET /api/suppliers` — supplier details
- `GET /api/orders` — purchase orders
- `POST /api/ai/analyze` — run agent analysis
- `POST /api/ai/chat` — ask the decision assistant (JSON body: `{"message":"Which inventory items are low?"}`)
