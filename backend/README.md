# FastAPI Backend

A modern FastAPI backend powered by Gel for data persistence, authentication, and authorization.

## 🚀 Quick Start

### Prerequisites

- **Python 3.12+** 
- **[uv](https://docs.astral.sh/uv/)** for Python package management

### Setup

Navigate to the backend directory:

```bash
cd backend
```

Install dependencies:

```bash
uv sync
```

### Development

Start the development server:

```bash
# Development server with auto-reload and Gel-powered data migrations
uv run fastapi dev
```

The API will be available at:
- **API Docs**: http://localhost:8000/docs
- **API**: http://localhost:8000/api/v1
- **Frontend**: http://localhost:8000 (served by FastAPI)

### Environment Setup

The backend reads configuration from a `.env` file in the project root. Key settings:

```env
# Development settings
ENVIRONMENT=local
PROJECT_NAME="Full Stack FastAPI Template"

# Gel configuration
GEL_AUTH_SIGNING_KEY=your-secret-key

# CORS settings (for frontend development)
BACKEND_CORS_ORIGINS=http://localhost:5173,http://localhost:3000
```

## 🏗️ Architecture

### Key Components

- **FastAPI App** (`app/main.py`): Main application with Gel integration
- **API Routes** (`app/api/`): RESTful API endpoints
- **Models** (`app/models/`): Auto-generated Gel models and utilities
- **Services** (`app/services/`): Business logic layer
- **Authentication**: Built-in Gel auth with `ext::auth`

### Development vs Production

**Development Mode** (`ENVIRONMENT=local`):
- Proxies frontend requests to Vite dev server
- Enables hot module reloading
- Detailed error messages

**Production Mode**:
- Serves built React app as static files
- Optimized for performance
- Error tracking with Sentry

## 🧪 Testing

### Run Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=app

# Run specific test file
uv run pytest app/tests/test_api_routes.py

# Run with verbose output
uv run pytest -v
```

### Test Structure

```
backend/app/tests/
├── conftest.py              # Test configuration and fixtures
├── test_api_routes.py       # API endpoint tests
└── test_user_impersonation_example.py  # Auth tests
```

### Writing Tests

Tests use pytest with Gel's testing utilities:

```python
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_items():
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
```

## 🗄️ Database Management

### Gel Integration

This backend uses Gel for data persistence:

- **Schema**: Defined in `dbschema/default.gel`
- **Auto-migrations**: Gel watches schema changes and applies them automatically
- **Auto-codegen**: Python client models regenerated automatically on schema changes
- **Queries**: Type-safe with auto-generated client

### Development Workflow

**During Development:**
Gel runs in "dev mode" with automatic schema watching:

```bash
# Initialize project (from project root)
gel project init

# Start development (schema changes applied automatically)
./scripts/dev  # or uv run fastapi dev
```

When you modify `dbschema/default.gel`, Gel automatically:
- Applies schema changes to the development database
- Regenerates Python client models
- No manual intervention needed!

**Committing Changes:**
When you're finished with your feature:

```bash
# Stop the dev service first
# Then commit your schema changes:

# 1. Create migration for your changes
gel migration create

# 2. Fast-forward migration history (schema already applied)
gel migrate --dev-mode
```

### Common Commands

```bash
# Initialize project
gel project init

# Start dev mode (automatic schema watching)
gel instance start

# Create migration after development
gel migration create

# Open interactive shell
gel
```

## 🔧 Development Workflow

### Code Organization

```
backend/app/
├── api/                    # API routes
│   ├── main.py            # API router
│   ├── deps.py            # Dependencies
│   └── routes/            # Route modules
├── core/                  # Core configuration
│   └── config.py          # Settings
├── models/                # Auto-generated Gel models
├── services/              # Business logic
└── main.py                # FastAPI application
```

### Adding New Features

1. **Start development**: `./scripts/dev` (enables schema watching)
2. **Update schema** in `dbschema/default.gel` (changes applied automatically)
3. **Add API routes** in `app/api/routes/` (models auto-generated)
4. **Implement business logic** in `app/services/`
5. **Write tests** in `app/tests/`
6. **Commit schema changes**:
   ```bash
   # When feature is complete
   gel migration create
   gel migrate --dev-mode
   ```

### Code Quality

```bash
# Lint code
uv run ruff check .

# Format code
uv run ruff format .

# Type checking
uv run mypy .
```

## 🔐 Authentication & Authorization

### Built-in Auth

Gel provides comprehensive authentication:

```python
# In your API routes
@app.get("/protected")
async def protected_route(
    current_user: User = fastapi.Depends(get_current_user)
):
    return {"user": current_user}
```

### Access Policies

Define authorization rules in your Gel schema:

```edgeql
# In dbschema/default.gel
type User {
    required email: str;
    full_name: str;
    
    access policy own_user
        allow all
        using (.identity = global ext::auth::ClientTokenIdentity);
}
```

## 🚀 Production Deployment

### Build

```bash
# Ensure dependencies are installed
uv sync --frozen

# Run the production server
uv run fastapi run app/main.py
```

### Environment Variables

Set these for production:

```env
ENVIRONMENT=production
PROJECT_NAME="Your App Name"
GEL_AUTH_SIGNING_KEY=secure-random-key
SENTRY_DSN=your-sentry-dsn
BACKEND_CORS_ORIGINS=https://yourdomain.com
```

## 📚 Learn More

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Gel Documentation](https://geldata.com/docs)
- [EdgeDB Tutorial](https://docs.edgedb.com/tutorial)
- [Pydantic Documentation](https://docs.pydantic.dev/)

---

**💡 Tip**: Use the top-level `./scripts/dev` command for the full development environment!
