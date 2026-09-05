# GenAI-Powered Financial Fraud Detection & Analytics Platform

> AI-powered financial fraud detection and analytics platform with transaction risk scoring, explainable insights, dashboards, reports, and a GenAI chatbot.

An end-to-end financial fraud analysis platform that helps analysts upload transaction datasets, identify potentially fraudulent activity, investigate risk signals, generate explainable insights, and create reports from one workspace.

The project combines a React dashboard with a FastAPI backend and a modular analytics, ML, reporting, and conversational-assistant architecture.

## Highlights

- Upload and preview CSV, XLS, and XLSX transaction datasets
- Validate, clean, and preprocess data before analysis
- Calculate risk scores and flag suspicious transactions
- Explore fraud trends, KPIs, and transaction-level details in a dashboard
- Inspect explainability signals and analyst-oriented insights
- Generate downloadable reports and maintain analysis logs
- Use a contextual chatbot interface for fraud-analysis questions
- Manage projects, settings, feedback, and session-aware workflows

## Architecture

```text
React + Vite frontend
        |
        | HTTP / JSON
        v
FastAPI application (/api/v1)
        |
        +-- Upload, validation, cleaning, preprocessing
        +-- Detection, analytics, dashboard, explainability
        +-- Reports, logs, projects, settings, feedback, chatbot
        +-- ML, NLP, agent orchestration utilities
        |
        v
SQLite by default / PostgreSQL or Supabase-compatible Postgres in production
```

## Tech Stack

| Area | Technologies |
| --- | --- |
| Frontend | React 19, TypeScript, Vite, Tailwind CSS, React Router |
| UI & visualization | Framer Motion, Recharts, Lucide Icons |
| Forms & validation | React Hook Form, Zod |
| Backend | FastAPI, Pydantic Settings, SQLAlchemy, Alembic |
| Data & ML | Pandas, NumPy, scikit-learn, PyArrow, Joblib |
| Database | SQLite for local development; PostgreSQL/Supabase-compatible Postgres supported |

## Project Structure

```text
.
├── app/
│   ├── backend/
│   │   ├── api/                 # API router and dependencies
│   │   ├── agents/              # Agent contracts and orchestration
│   │   ├── core/                # Configuration, security, exceptions
│   │   ├── db/                  # SQLAlchemy models and repositories
│   │   └── modules/             # Feature modules and controllers
│   └── frontend/
│       ├── components/          # Reusable UI components
│       ├── pages/               # Application screens
│       ├── services/            # API/mock data services
│       └── styles/              # Global styles and animations
├── data/                        # Local uploads, processed files, reports, logs
├── migrations/                  # Alembic migrations
├── models/                      # Trained model and vector-store artifacts
├── tests/                       # Backend, analytics, security, and contract tests
├── requirements.txt
└── .env.example
```

## Getting Started

### Prerequisites

- Python 3.11 or later
- Node.js 20 or later
- npm 10 or later

### 1. Configure environment variables

From the repository root, create your local configuration file from the template.

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Set a strong `SECRET_KEY` before any production deployment. Never commit `.env`; it is intentionally ignored by Git.

### 2. Start the backend

```bash
python -m venv .venv
```

Activate the virtual environment, then install dependencies:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
uvicorn app.backend.main:app --reload
```

The API starts at `http://127.0.0.1:8000`. Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

### 3. Start the frontend

In a second terminal:

```bash
cd app/frontend
npm install
npm run dev
```

Open `http://localhost:5173` in your browser.

### Production frontend build

```bash
cd app/frontend
npm run build
npm run preview
```

## Configuration

The application has safe defaults for local use, including a local SQLite database. Important environment variables include:

| Variable | Purpose |
| --- | --- |
| `APP_NAME` | Name displayed by the API |
| `ENVIRONMENT` | Runtime environment, such as `development` or `production` |
| `APP_DEBUG` | Enables FastAPI debug mode when `true` |
| `SECRET_KEY` | Secret used for application security tokens; use a long random value |
| `DATABASE_URL` | SQLAlchemy database URL; SQLite is used by default |
| `DATABASE_POOL_PRE_PING` | Checks database connections before reuse |
| `SUPABASE_URL` | Optional Supabase project URL |
| `SUPABASE_ANON_KEY` | Optional Supabase browser-safe key |
| `SUPABASE_SERVICE_ROLE_KEY` | Optional privileged server-side Supabase key; keep secret |

For Supabase Postgres, set `DATABASE_URL` to the Postgres connection URI from the Supabase dashboard. A project URL or publishable key alone is not a database connection string.

## API Overview

All feature routes are grouped under `/api/v1`. The API includes modules for:

- Authentication and project management
- File uploads and dataset validation
- Cleaning and preprocessing
- Fraud detection, analytics, and dashboard data
- Explainability, reports, and audit logs
- Settings, chatbot interactions, and analyst feedback

Basic health endpoints:

```text
GET /          # Service status
GET /health    # Health and database configuration status
```

Refer to `/docs` while the backend is running for the complete, live OpenAPI contract.

## Testing

Install the backend dependencies and run:

```bash
python -m pytest -q
```

The test suite covers analytics behavior, API responses, frontend contracts, security, session isolation, and project plan checks.

## Security Notes

- Do not commit `.env`, credentials, exports containing sensitive data, local uploads, model artifacts, dependency folders, or generated caches.
- Rotate any credential that was ever accidentally committed to version control.
- Use environment-specific `DATABASE_URL` and `SECRET_KEY` values in deployment.
- Restrict CORS origins to the deployed frontend domain before production release.

## Current Status

The frontend provides a complete analyst-facing experience and includes realistic mock services where API integration is still being developed. The backend exposes a modular FastAPI foundation for the corresponding workflows and can be extended with production data sources, trained fraud models, authentication providers, and deployment infrastructure.

## Author

**Vansh Tiwari**

## License

This project is intended for educational and portfolio use. Add a license file before distributing or using it in production.
