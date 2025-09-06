# Changelog

This changelog references changes made both to the FastAPI backend, `fastapi_backend`, and the
frontend TypeScript client, `nextjs-frontend`.

!!! note
    The backend and the frontend are versioned together, that is, they have the same version number.
    When you update the backend, you should also update the frontend to the same version.

## 0.1.0 <small>September 6, 2025</small> {id="0.1.0"}

### Added
- **Full-Stack Architecture**: Complete RCM platform with FastAPI backend and Next.js frontend
- **AI Integration**: PyTorch-based denial prediction model with real-time inference
- **Docker Containerization**: Multi-service setup with PostgreSQL, MailHog, and auto-reload
- **Authentication System**: FastAPI Users with JWT authentication, registration, and password reset
- **Database Integration**: PostgreSQL with SQLAlchemy and Alembic migrations
- **API Documentation**: Interactive FastAPI docs at `/docs` and OpenAPI schema
- **Email Testing**: MailHog integration for development email testing
- **Health Check Endpoint**: `/health` for monitoring service status
- **Comprehensive Setup Guide**: Updated README with Docker-first installation
- **Dependency Management**: uv for Python, pnpm for Node.js

### Fixed
- Docker container startup issues with executable permissions and environment variables
- PyTorch installation in Docker with custom index configuration
- Model file path errors in denial predictor
- Import and dependency resolution issues

### Technical Details
- **Backend**: FastAPI with Python 3.12, PyTorch 2.8.0, PostgreSQL async driver
- **Frontend**: Next.js 15 with TypeScript, Tailwind CSS
- **Infrastructure**: Docker Compose with 6 services, hot-reload enabled
- **AI Model**: Simple neural network for denial prediction (trainable at runtime)

## 0.0.6 <small>September 1, 2025</small> {id="0.0.6"}

- Upgrade Next.js version to 15.5.0

## 0.0.5 <small>July 9, 2025</small> {id="0.0.5"}

- Items Pagination

## 0.0.4 <small>July 9, 2025</small> {id="0.0.4"}

- Fix ESlint missing for pre-commit

## 0.0.3 <small>April 23, 2025</small> {id="0.0.3"}

- Created docs

## 0.0.2 <small>March 12, 2025</small> {id="0.0.2"}

- Generate release draft using github actions

## 0.0.1 <small>March 12, 2025</small> {id="0.0.1"}

- Initial release
