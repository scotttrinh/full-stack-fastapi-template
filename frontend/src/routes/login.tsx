import { Container, Image, Input, Text } from "@chakra-ui/react";
import {
  Link as RouterLink,
  createFileRoute,
  redirect,
} from "@tanstack/react-router";
import { useForm } from "@tanstack/react-form";
import { FiLock, FiMail } from "react-icons/fi";
import { z } from "zod/v4-mini";

import type { Body_login_login_access_token as AccessToken } from "@/client";
import { Button } from "@/components/ui/button";
import { Field } from "@/components/ui/field";
import { InputGroup } from "@/components/ui/input-group";
import { PasswordInput } from "@/components/ui/password-input";
import useAuth, { isLoggedIn } from "@/hooks/useAuth";
import Logo from "/assets/images/fastapi-logo.svg";
import { Email, Password } from "@/utils";

const LoginForm = z.object({
  username: Email,
  password: Password,
});

export const Route = createFileRoute("/login")({
  component: Login,
  beforeLoad: async () => {
    if (isLoggedIn()) {
      throw redirect({
        to: "/",
      });
    }
  },
});

function Login() {
  const { loginMutation, error, resetError } = useAuth();
  const form = useForm({
    validators: {
      onBlur: LoginForm,
    },
    onSubmit: async ({ value, formApi }) => {
      if (formApi.state.isSubmitting) return;

      resetError();

      try {
        await loginMutation.mutateAsync(value);
      } catch {
        // error is handled by useAuth hook
      }
    },
    defaultValues: {
      username: "",
      password: "",
    },
  });

  return (
    <>
      <Container
        as="form"
        onSubmit={form.handleSubmit}
        h="100vh"
        maxW="sm"
        alignItems="stretch"
        justifyContent="center"
        gap={4}
        centerContent
      >
        <Image
          src={Logo}
          alt="FastAPI logo"
          height="auto"
          maxW="2xs"
          alignSelf="center"
          mb={4}
        />
        <form.Field name="username">
          {(field) => (
            <Field
              invalid={!field.state.meta.isValid}
              errorText={field.state.meta.errors.join(", ")}
            >
              <InputGroup w="100%" startElement={<FiMail />}>
                <Input
                  id="username"
                  value={field.state.value ?? ""}
                  onChange={(e) => field.handleChange(e.target.value)}
                  placeholder="Email"
                  type="email"
                />
              </InputGroup>
            </Field>
          )}
        </form.Field>

        <form.Field name="password">
          {(field) => (
            <PasswordInput
              type="password"
              startElement={<FiLock />}
              value={field.state.value ?? ""}
              onChange={(e) => field.handleChange(e.target.value)}
              placeholder="Password"
              isInvalid={!field.state.meta.isValid}
              errorText={field.state.meta.errors.join(", ")}
            />
          )}
        </form.Field>
        <RouterLink to="/recover-password" className="main-link">
          Forgot Password?
        </RouterLink>
        <Button variant="solid" type="submit" loading={form.state.isSubmitting} size="md">
          Log In
        </Button>
        <Text>
          Don't have an account?{" "}
          <RouterLink to="/signup" className="main-link">
            Sign Up
          </RouterLink>
        </Text>
      </Container>
    </>
  );
}
