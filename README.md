# Full Stack FastAPI Template

A modern, production-ready full-stack template built with FastAPI, Gel, and React.

## 🚀 Technology Stack and Features

### Backend
- ⚡ [**FastAPI**](https://fastapi.tiangolo.com) - Modern, fast Python web framework
- 🧰 [**Gel**](https://geldata.com) - Next-generation data layer powered by PostgreSQL
  - 🔐 Built-in authentication with `ext::auth`
  - 🛡️ Schema-level access policies for authorization
  - 🎯 Type-safe database queries with auto-generated Python client
- 🔍 [**Pydantic**](https://docs.pydantic.dev) - Data validation and settings management
- ✅ [**Pytest**](https://pytest.org) - Testing framework

### Frontend
- ⚛️ [**React**](https://react.dev) - Modern frontend framework
- 🏗️ [**TypeScript**](https://www.typescriptlang.org/) - Type safety throughout
- ⚡ [**Vite**](https://vitejs.dev/) - Lightning-fast build tool
- 🎨 [**Chakra UI**](https://chakra-ui.com) - Simple, modular component library
- 📋 [**TanStack Form**](https://tanstack.com/form) - Powerful form management
- 🤖 Auto-generated API client from OpenAPI schema
- 🧪 [**Playwright**](https://playwright.dev) - End-to-end testing
- 🦇 Dark mode support

### Development & Deployment
- 🚀 **One-command development** - `./scripts/dev` starts everything
- 🔄 **Auto-migrations** - Gel watches schema changes and applies them automatically
- 🤖 **Auto-codegen** - Models regenerated automatically on schema changes
- 🔥 **Hot module reloading** - Backend proxies to Vite dev server
- 🚢 **Simplified deployment** - React app served directly from FastAPI
- 🏭 **GitHub Actions** - CI/CD pipeline included
- 🔧 **Modern tooling** - UV for Python, Vite for frontend, Gel for data

## ✨ Quick Start

### Prerequisites

- **Python 3.12+** with [uv](https://docs.astral.sh/uv/) package manager
- **Node.js 18+** with npm
- **Gel CLI** - Install with `curl -sSfL https://sh.gel.dev | sh`

### 🚀 One-Command Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd full-stack-fastapi-template

# Run the setup script
./scripts/setup
```

### 🏃‍♂️ Start Development

```bash
# Start the full development environment
./scripts/dev
```

This will start:
- **Gel database**
- **FastAPI backend** on `http://localhost:8000`
- **Vite frontend** on `http://localhost:5173` (with hot reload)

The backend automatically proxies to the Vite dev server for seamless development with hot module reloading.

**✨ Development Features:**
- **Schema watching**: Modify `dbschema/default.gel` and see changes applied instantly
- **Auto-codegen**: Python models regenerated automatically on schema changes  
- **Hot reloading**: Frontend changes reflect immediately via Vite
- **Integrated API**: Backend and frontend work together seamlessly

### 🧪 Run Tests

```bash
# Run all tests
./scripts/test

# For CI environments
./scripts/test-ci
```


## 🔧 Local Configuration

Copy the `.env.example` file to `.env` and configure

```bash
cp .env.example .env
```

## 🛠️ Development Scripts

The project includes several convenience scripts in `./scripts/`:

- **`./scripts/setup`** - One-time project setup (dependencies, database, client generation)
- **`./scripts/dev`** - Start full development environment (database + backend + frontend)
- **`./scripts/test`** - Run all tests (backend + frontend)
- **`./scripts/test-ci`** - Run tests in CI environment
- **`./scripts/generate-client.sh`** - Generate frontend API client from backend OpenAPI schema

These scripts handle the coordination between Gel, FastAPI, and Vite for a seamless development experience.

### 🔄 Schema Development Workflow

During development, Gel automatically watches for schema changes:

1. **Start development**: `./scripts/dev`
2. **Edit schema**: Modify `dbschema/default.gel`
3. **Instant updates**: Changes applied automatically + models regenerated
4. **Iterate freely**: Make as many changes as needed

When your feature is complete:

```bash
# Commit your schema changes
gel migration create        # Create migration from your changes
gel migrate --dev-mode     # Fast-forward migration history
```

## 🏗️ Project Structure

```
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/            # API routes
│   │   ├── models/         # Auto-generated Gel models
│   │   ├── services/       # Business logic
│   │   └── main.py         # FastAPI app + React hosting
│   └── pyproject.toml      # Python dependencies
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── hooks/          # Custom hooks
│   │   ├── routes/         # Page components and routing
│   │   └── client/         # Auto-generated API client
│   └── package.json        # Node.js dependencies
├── dbschema/               # Gel database schema
│   ├── default.gel         # Main schema file
│   └── migrations/         # Database migrations
├── scripts/                # Development and build scripts
│   ├── dev                 # Start development environment
│   ├── setup               # One-time project setup
│   ├── test                # Run all tests
│   └── generate-client.sh  # Generate API client
└── gel.toml               # Gel configuration
```

## 🔐 Authentication & Authorization

This template uses Gel's built-in authentication system.

- **Authentication**: Handled by `ext::auth` extension
- **Authorization**: Schema-level access policies in `dbschema/default.gel`

## 🧪 Testing

### Run All Tests

```bash
# Run all tests (backend + frontend)
./scripts/test

# For CI environments
./scripts/test-ci
```

### Individual Test Suites

**Backend Tests:**
```bash
cd backend
uv run pytest

# With coverage
uv run pytest --cov=app
```

**Frontend Tests:**
```bash
cd frontend

# Unit/integration tests
npm run test

# End-to-end tests
npm run test:e2e
```

## 🚀 Production Deployment

### Build for Production

```bash
# Build frontend
cd frontend
npm run build

# The built files are automatically served by FastAPI
cd ../backend
uv run fastapi run app/main.py
```

### Environment Setup

For production, ensure you have:

1. A production Gel instance (Gel Cloud or self-hosted)
2. Environment variables properly configured
3. HTTPS enabled
4. Proper secret key rotation

## 📚 Development Guides

- [Backend Development](./backend/README.md) - FastAPI and Gel details
- [Frontend Development](./frontend/README.md) - React and TypeScript setup
- [Database Schema](./dbschema/README.md) - Gel schema and migrations
- [Deployment Guide](./deployment.md) - Production deployment options

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Built with ❤️ using FastAPI, Gel, and React**
