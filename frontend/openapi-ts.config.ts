import { defineConfig } from "@hey-api/openapi-ts";

export default defineConfig({
  input: "./openapi.json",
  output: "./src/client",
  // exportSchemas: true,
  plugins: [
    "legacy/axios",
    {
      name: "@hey-api/sdk",
      // NOTE: this doesn't allow tree-shaking
      asClass: true,
      operationId: true,
      methodNameBuilder: (operation) => {
        // @ts-expect-error - operation.name is not typed
        let name: string = operation.name as string;
        // @ts-expect-error - operation.service is not typed
        const service: string = operation.service as string;

        if (service && name.toLowerCase().startsWith(service.toLowerCase())) {
          name = name.slice(service.length);
        }

        return name.charAt(0).toLowerCase() + name.slice(1);
      },
    },
  ],
});
