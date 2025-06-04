import { Container, Flex, Image, Input } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { useForm } from "@tanstack/react-form";
import { FiUser } from "react-icons/fi";
import { z } from "zod/v4-mini";

import { Button } from "@/components/ui/button";
import { Field } from "@/components/ui/field";
import { InputGroup } from "@/components/ui/input-group";
import useAuth from "@/hooks/useAuth";
import Logo from "/assets/images/fastapi-logo.svg";
import { formatErrors } from "@/utils";

export const Route = createFileRoute("/signup")({
  component: SignUp,
  validateSearch: z.object({
    email: z.optional(z.string().check(z.email())),
  }),
});

const NewUserProfileForm = z.object({
  full_name: z.string().check(z.trim(), z.minLength(1)),
  email: z.string().check(z.trim(), z.minLength(1), z.email()),
});
type NewUserProfileForm = z.output<typeof NewUserProfileForm>;

function SignUp() {
  const { signUpMutation } = useAuth();
  const { email } = Route.useSearch();

  const form = useForm({
    validators: {
      onSubmit: NewUserProfileForm,
    },
    defaultValues: {
      full_name: "",
      email: email ?? "",
    } as NewUserProfileForm,
    onSubmit: async ({ value }) => {
      await signUpMutation.mutateAsync({ ...value, password: "" });
    },
  });

  return (
    <>
      <Flex flexDir={{ base: "column", md: "row" }} justify="center" h="100vh">
        <Container
          as="form"
          onSubmit={() => void form.handleSubmit()}
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
          <form.Field name="full_name">
            {(field) => (
              <Field
                invalid={!field.state.meta.isValid}
                errorText={formatErrors(field.state.meta.errors)}
              >
                <InputGroup w="100%" startElement={<FiUser />}>
                  <Input
                    id="full_name"
                    minLength={3}
                    value={field.state.value}
                    onChange={(e) => field.handleChange(e.target.value)}
                    placeholder="Full Name"
                    type="text"
                  />
                </InputGroup>
              </Field>
            )}
          </form.Field>
          <form.Field name="email">
            {(field) => (
              <Field
                invalid={!field.state.meta.isValid}
                errorText={formatErrors(field.state.meta.errors)}
              >
                <InputGroup w="100%" startElement={<FiUser />}>
                  <Input
                    id="email"
                    value={field.state.value}
                    onChange={(e) => field.handleChange(e.target.value)}
                    placeholder="Email"
                    type="email"
                  />
                </InputGroup>
              </Field>
            )}
          </form.Field>

          <Button
            variant="solid"
            type="submit"
            loading={form.state.isSubmitting}
          >
            Save Profile
          </Button>
        </Container>
      </Flex>
    </>
  );
}

export default SignUp;
