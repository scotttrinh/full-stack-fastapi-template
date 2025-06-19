// Updated to use Gel auth registration endpoint
import { OpenAPI, GelAuthService } from "../../src/client";

OpenAPI.BASE = `${process.env.VITE_API_URL}`;

export const createUser = async ({
  email,
  password,
}: {
  email: string;
  password: string;
}) => {
  return await GelAuthService.gelAuthEmailPasswordSignUp({
    requestBody: {
      email,
      password,
      full_name: "Test User",
    },
  });
};
