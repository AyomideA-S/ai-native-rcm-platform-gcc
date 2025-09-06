# AI-Native RCM Platform for GCC Healthcare

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

An AI-powered Revenue Cycle Management (RCM) platform reimagining healthcare administration in the GCC. Automates eligibility checks, prior authorizations, coding, claims scrubbing, denial management, and reconciliation to reduce paperwork and boost efficiency.

## About The Project

This prototype aligns with Humaein's vision of "patients, not paperwork" by using AI agents for end-to-end RCM workflows. Key features include ML-based denial prediction (PyTorch), modular pipelines (Dagster), and compliance with GCC regulations (e.g., DHA/MOH).

Built With:

- [FastAPI](https://fastapi.tiangolo.com/) (Backend API)
- [Next.js](https://nextjs.org/) (Frontend UI)
- [PyTorch](https://pytorch.org/) (ML Models for Denial Prediction)
- [PostgreSQL](https://www.postgresql.org/) (Database)
- [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/) (Containerization)
- [uv](https://github.com/astral-sh/uv) (Python Dependency Management)
- [pnpm](https://pnpm.io/) (Node.js Package Management)
- [MailHog](https://github.com/mailhog/MailHog) (Email Testing)

## Getting Started

Follow these steps to set up and run the project locally using Docker.

### Prerequisites

- **Docker**: Version 20.10 or later ([Install Docker](https://docs.docker.com/get-docker/))
- **Docker Compose**: Version 2.0 or later (usually included with Docker Desktop)
- **Git**: For cloning the repository

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AyomideA-S/ai-native-rcm-platform-gcc.git
   cd ai-native-rcm-platform-gcc
   ```

2. **Set Up Environment Variables**:
   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and fill in the required variables (database credentials, API keys, etc.). The file includes settings for PostgreSQL, email, and other services.

3. **Build and Run with Docker Compose**:
   ```bash
   docker compose up --build
   ```
   - This will build the images and start all services:
     - **Backend** (FastAPI): `http://localhost:8000`
     - **Frontend** (Next.js): `http://localhost:3000`
     - **Database** (PostgreSQL): Port 5432
     - **MailHog** (Email Testing): `http://localhost:8025`
   - The first build may take time due to PyTorch installation.

4. **Verify Setup**:
   - Backend API Docs: `http://localhost:8000/docs`
   - Health Check: `http://localhost:8000/health`
   - Frontend Dashboard: `http://localhost:3000`
   - Database: Accessible via `postgresql://postgres:password@localhost:5432/rcm_db`
   - Email Testing: `http://localhost:8025`

### Local Development (Optional)

If you prefer running services locally without Docker:

1. **Backend Setup**:
   - Install Python 3.12 and uv
   - `cd fastapi_backend`
   - `uv sync` (installs dependencies including PyTorch)
   - `uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

2. **Frontend Setup**:
   - Install Node.js 18+ and pnpm
   - `cd nextjs-frontend`
   - `pnpm install`
   - `pnpm dev`

3. **Database**:
   - Run PostgreSQL locally or use Docker for just the DB: `docker compose up db`

## Usage

1. **Access the Application**:
   - Frontend: `http://localhost:3000` (Next.js dashboard)
   - Backend API: `http://localhost:8000/docs` (FastAPI interactive docs)

2. **Test AI Features**:
   - Use the `/predict-denial/` endpoint to test denial prediction
   - Input sample patient/claim data via the API or frontend

3. **Database Management**:
   - Use tools like pgAdmin or DBeaver to connect to `localhost:5432`
   - Alembic migrations are handled automatically in Docker

4. **Email Testing**:
   - View sent emails at `http://localhost:8025`

## Project Structure

```
ai-native-rcm-platform-gcc/
├── fastapi_backend/          # FastAPI backend
│   ├── app/                  # Main application code
│   ├── Dockerfile            # Backend container config
│   ├── pyproject.toml        # Python dependencies
│   └── uv.lock               # Dependency lock file
├── nextjs-frontend/          # Next.js frontend
│   ├── app/                  # Next.js app directory
│   ├── Dockerfile            # Frontend container config
│   └── package.json          # Node dependencies
├── docker-compose.yml        # Multi-service orchestration
├── .env.example              # Environment variables template
└── README.md                 # This file
```

## Development Notes

- **Hot Reload**: Enabled for both backend and frontend in development
- **Database Migrations**: Handled by Alembic (runs automatically in Docker)
- **Model Files**: PyTorch models (`.pth` files) are generated at runtime and not committed to Git
- **Environment**: Uses Python 3.12, Node.js 18+, PostgreSQL 17

## Roadmap

- [ ] Integrate real EMR APIs (e.g., Epic, Cerner)
- [ ] Add LLM for appeal drafting (LangChain integration)
- [ ] Enhance ML accuracy with real GCC healthcare datasets
- [ ] Implement CI/CD pipeline for GCP/Azure deployment
- [ ] Add comprehensive testing suite

See [open issues](https://github.com/AyomideA-S/ai-native-rcm-platform-gcc/issues) for details.

## Contributing

Contributions welcome! 

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/AmazingFeature`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact

Ayomide Ayodele-Soyebo - midesuperbest@gmail.com

Project Link: https://github.com/AyomideA-S/ai-native-rcm-platform-gcc

## Acknowledgments

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Next.js Documentation](https://nextjs.org/docs)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- Inspired by AI healthcare startups like AKASA and Innovaccer
