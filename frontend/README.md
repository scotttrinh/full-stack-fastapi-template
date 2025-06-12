# Frontend - React + TypeScript + Vite

The frontend is built with modern tools and libraries:

- ⚡ [**Vite**](https://vitejs.dev/) - Lightning-fast build tool and dev server
- ⚛️ [**React**](https://reactjs.org/) - Modern frontend framework
- 🏗️ [**TypeScript**](https://www.typescriptlang.org/) - Type safety throughout
- 🎨 [**Chakra UI**](https://chakra-ui.com/) - Simple, modular component library
- 📋 [**TanStack Form**](https://tanstack.com/form) - Powerful form management
- 🔄 [**TanStack Query**](https://tanstack.com/query) - Data fetching and caching
- 🧭 [**TanStack Router**](https://tanstack.com/router) - Type-safe routing
- 🤖 **Auto-generated API client** - From FastAPI OpenAPI schema

## 🚀 Quick Start

### Prerequisites

- **Node.js 18+** with npm
- Backend server running on `http://localhost:8000`

### Setup

Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Generate the API client from your running backend:

```bash
cd ..
./scripts/generate-client.sh
```

Start the development server:

```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

## 🔧 Development Workflow

### Node.js Version Management

This project uses Node.js version specified in `.nvmrc`. If you have `fnm` or `nvm` installed:

```bash
# Using fnm (recommended)
fnm install && fnm use

# Using nvm
nvm install && nvm use
```

### API Client Generation

The frontend uses an auto-generated client based on your FastAPI OpenAPI schema.

**Automatic Generation:**

```bash
# From the project root
./scripts/generate-client.sh
```

**Manual Generation:**

```bash
# Make sure your backend is running on localhost:8000
npm run generate-client
```

> **Note:** Regenerate the client whenever you change your FastAPI API endpoints or models.

### Environment Configuration

Create a `.env` file in the `frontend` directory for local overrides:

```env
# API URL (defaults to http://localhost:8000)
VITE_API_URL=http://localhost:8000

# For production or remote API
# VITE_API_URL=https://api.your-domain.com
```

## 📁 Project Structure

```
frontend/
├── src/
│   ├── assets/          # Static assets (images, icons)
│   ├── client/          # Auto-generated API client
│   ├── components/      # Reusable React components
│   ├── hooks/           # Custom React hooks
│   ├── routes/          # Page components and routing
│   ├── theme.tsx        # Chakra UI theme configuration
│   └── main.tsx         # Application entry point
├── tests/               # End-to-end tests
├── public/              # Static files served directly
└── package.json         # Dependencies and scripts
```

## 🧪 Testing

### Unit & Integration Tests

```bash
npm run test
```

### End-to-End Tests with Playwright

Make sure your backend is running, then:

```bash
# Run tests headlessly
npm run test:e2e

# Run tests with UI (interactive)
npx playwright test --ui

# Run specific test file
npx playwright test tests/auth.spec.ts
```

### Test Development

- Tests are located in the `tests/` directory
- Use Playwright for end-to-end testing
- Mock API responses when needed for isolated testing

## 🏗️ Key Technologies

### TanStack Form

This template uses TanStack Form for form management:

```tsx
import { useForm } from "@tanstack/react-form";

function MyForm() {
  const form = useForm({
    defaultValues: {
      email: "",
      password: "",
    },
    onSubmit: async ({ value }) => {
      // Handle form submission
    },
  });

  // Form implementation...
}
```

### TanStack Query

For data fetching and caching:

```tsx
import { useQuery } from "@tanstack/react-query";
import { ItemsService } from "../client";

function ItemsList() {
  const { data: items, isLoading } = useQuery({
    queryKey: ["items"],
    queryFn: () => ItemsService.readItems(),
  });

  // Component implementation...
}
```

### Chakra UI

For consistent, accessible UI components:

```tsx
import { Box, Button, VStack } from "@chakra-ui/react";

function MyComponent() {
  return (
    <Box p={4}>
      <VStack spacing={4}>
        <Button colorScheme="blue">Click me</Button>
      </VStack>
    </Box>
  );
}
```

## 🚀 Production Build

Build the frontend for production:

```bash
npm run build
```

The built files will be in the `dist/` directory and are automatically served by the FastAPI backend in production.

Preview the production build locally:

```bash
npm run preview
```

## 🔧 Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run test` - Run unit tests
- `npm run test:e2e` - Run end-to-end tests
- `npm run generate-client` - Generate API client
- `npm run lint` - Run ESLint
- `npm run format` - Format code with Prettier

## 🎨 Customization

### Theme

Customize the Chakra UI theme in `src/theme.tsx`:

```tsx
import { extendTheme } from "@chakra-ui/react";

const theme = extendTheme({
  colors: {
    brand: {
      50: "#your-color",
      // ... more colors
    },
  },
  // ... more theme customizations
});
```

### Components

Create reusable components in `src/components/`:

```tsx
// src/components/MyComponent.tsx
import { Box, BoxProps } from "@chakra-ui/react";

interface MyComponentProps extends BoxProps {
  customProp?: string;
}

export function MyComponent({ customProp, ...props }: MyComponentProps) {
  return <Box {...props}>Content</Box>;
}
```

## 🔗 Integration with Backend

The frontend integrates seamlessly with the FastAPI backend:

- **Authentication**: Uses Gel's built-in auth system
- **API Client**: Auto-generated from OpenAPI schema
- **Type Safety**: Full TypeScript support end-to-end
- **Production**: Served directly from FastAPI server

## 📚 Learn More

- [Vite Documentation](https://vitejs.dev/guide/)
- [React Documentation](https://react.dev/)
- [TanStack Form](https://tanstack.com/form)
- [TanStack Query](https://tanstack.com/query)
- [Chakra UI](https://chakra-ui.com/docs)
- [Playwright Testing](https://playwright.dev/docs/intro)
