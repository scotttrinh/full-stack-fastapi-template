import { Box, Button, Container, Heading, VStack } from "@chakra-ui/react";
import { useMutation } from "@tanstack/react-query";
import { useForm } from "@tanstack/react-form";
import { FiLock } from "react-icons/fi";

import { type ApiError, type UpdatePassword, UsersService } from "@/client";
import useCustomToast from "@/hooks/useCustomToast";
import { confirmPasswordRules, handleError, passwordRules } from "@/utils";
import { PasswordInput } from "../ui/password-input";

interface UpdatePasswordForm extends UpdatePassword {
  confirm_password: string;
}

const ChangePassword = () => {
  const { showSuccessToast } = useCustomToast();
  const form = useForm({
    defaultValues: {
      current_password: "",
      new_password: "",
      confirm_password: "",
    } as UpdatePasswordForm,
    onSubmit: (data) => {
      mutation.mutate(data.value);
    },
  });

  const mutation = useMutation({
    mutationFn: (data: UpdatePassword) =>
      UsersService.updatePasswordMe({ requestBody: data }),
    onSuccess: () => {
      showSuccessToast("Password updated successfully.");
      form.reset();
    },
    onError: (err: ApiError) => {
      handleError(err);
    },
  });

  return (
    <>
      <Container maxW="full">
        <Heading size="sm" py={4}>
          Change Password
        </Heading>
        <Box as="form" onSubmit={form.handleSubmit}>
          <VStack gap={4} w={{ base: "100%", md: "sm" }}>
            <form.Field name="current_password">
              {(field) => (
                <PasswordInput
                  type="current_password"
                  startElement={<FiLock />}
                  placeholder="Current Password"
                  value={field.state.value}
                  onChange={(e) => field.handleChange(e.target.value)}
                  errors={field.state.meta.errors}
                />
              )}
            </form.Field>

            <form.Field name="new_password">
              {(field) => (
                <PasswordInput
                  type="new_password"
                  startElement={<FiLock />}
                  placeholder="New Password"
                  minLength={passwordRules().minLength.value}
                  value={field.state.value}
                  onChange={(e) => field.handleChange(e.target.value)}
                  errors={field.state.meta.errors}
                />
              )}
            </form.Field>

            <form.Field name="confirm_password" validators={{
              onBlur: ({ value }) => {
                if (value === form.state.values.new_password) {
                  return undefined;
                }
                return "The passwords do not match";
              }
            }}>
              {(field) => (
                <PasswordInput
                  type="confirm_password"
                  startElement={<FiLock />}
                  placeholder="Confirm Password"
                  value={field.state.value}
                  onChange={(e) => field.handleChange(e.target.value)}
                  errors={field.state.meta.errors}
                />
              )}
            </form.Field>
          </VStack>
          <Button
            variant="solid"
            mt={4}
            type="submit"
            loading={form.state.isSubmitting}
            disabled={!form.state.isValid}
          >
            Save
          </Button>
        </Box>
      </Container>
    </>
  );
};
export default ChangePassword;
