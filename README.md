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
- 🚢 **Simplified deployment** - React app served directly from FastAPI
- 🏭 **GitHub Actions** - CI/CD pipeline included
- 🔧 **Modern tooling** - UV for Python dependencies, ESLint, Prettier

## ✨ Quick Start

### Prerequisites

- **Python 3.12+** with [uv](https://docs.astral.sh/uv/) package manager
- **Node.js 18+** with npm

### 1. Clone and Setup

Clone the repository:

```bash
git clone <your-repo-url>
cd full-stack-fastapi-template
```

### 2. Database Setup

Start local Gel instances:

```bash
gel project init
```

### 3. Backend Setup

```bash
cd backend

# Install dependencies
uv sync

# Start the FastAPI development server
uv run fastapi dev app/main.py
```

The backend will be available at `http://localhost:8000`

### 4. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Generate API client from backend OpenAPI schema
npm run generate-client

# Start the Vite development server
npm run dev
```

The frontend will be available at `http://localhost:5173`

## 🔧 Local Configuration

Copy the `.env.example` file to `.env` and configure

```bash
cp .env.example .env
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
│   │   ├── pages/          # Page components
│   │   └── client/         # Auto-generated API client
│   └── package.json        # Node.js dependencies
├── dbschema/               # Gel database schema
│   ├── default.gel         # Main schema file
│   └── migrations/         # Database migrations
└── gel.toml               # Gel configuration
```

## 🔐 Authentication & Authorization

This template uses Gel's built-in authentication system.

- **Authentication**: Handled by `ext::auth` extension
- **Authorization**: Schema-level access policies in `dbschema/default.gel`

## 🧪 Testing

### Backend Tests

```bash
cd backend
uv run pytest
```

### Frontend Tests

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
