import {
  Box,
  Button,
  Container,
  Flex,
  Heading,
  Input,
  Text,
} from "@chakra-ui/react";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { useState } from "react";
import { useForm } from "@tanstack/react-form";
import { z } from "zod/v4-mini";

import {
  type ApiError,
  type UserPublic,
  type UserUpdateMe,
  UsersService,
} from "@/client";
import useAuth from "@/hooks/useAuth";
import useCustomToast from "@/hooks/useCustomToast";
import { Email, handleError } from "@/utils";
import { Field } from "../ui/field";

const UserUpdateMeForm = z.partial(
  z.object({
    full_name: z
      .string()
      .check(z.maxLength(256, "Full name must be less than 256 characters")),
    email: Email,
  })
);

const UserInformation = () => {
  const queryClient = useQueryClient();
  const { showSuccessToast } = useCustomToast();
  const [editMode, setEditMode] = useState(false);
  const { user: currentUser } = useAuth();
  const form = useForm({
    validators: {
      onBlur: UserUpdateMeForm,
    },
    onSubmit: (data) => {
      mutation.mutate(data.value);
    },
    defaultValues: {
      full_name: currentUser?.full_name,
      email: currentUser?.email,
    } as UserUpdateMe,
  });

  const toggleEditMode = () => {
    setEditMode(!editMode);
  };

  const mutation = useMutation({
    mutationFn: (data: UserUpdateMe) =>
      UsersService.updateUserMe({ requestBody: data }),
    onSuccess: () => {
      showSuccessToast("User updated successfully.");
    },
    onError: (err: ApiError) => {
      handleError(err);
    },
    onSettled: () => {
      queryClient.invalidateQueries();
    },
  });

  const onCancel = () => {
    form.reset();
    toggleEditMode();
  };

  return (
    <>
      <Container maxW="full">
        <Heading size="sm" py={4}>
          User Information
        </Heading>
        <Box
          w={{ sm: "full", md: "sm" }}
          as="form"
          onSubmit={form.handleSubmit}
        >
          <form.Field name="full_name">
            {(field) => (
              <Field
                label="Full name"
                invalid={!field.state.meta.isValid}
                errorText={field.state.meta.errors.join(", ")}
              >
                {editMode ? (
                  <Input
                    type="text"
                    size="md"
                    value={field.state.value ?? ""}
                    onChange={(e) => field.handleChange(e.target.value)}
                  />
                ) : (
                  <Text
                    fontSize="md"
                    py={2}
                    color={!currentUser?.full_name ? "gray" : "inherit"}
                    truncate
                    maxW="sm"
                  >
                    {currentUser?.full_name || "N/A"}
                  </Text>
                )}
              </Field>
            )}
          </form.Field>
          <form.Field name="email">
            {(field) => (
              <Field
                mt={4}
                label="Email"
                invalid={!field.state.meta.isValid}
                errorText={field.state.meta.errors.join(", ")}
              >
                {editMode ? (
                  <Input
                    value={field.state.value ?? ""}
                    onChange={(e) => field.handleChange(e.target.value)}
                    type="email"
                    size="md"
                  />
                ) : (
                  <Text fontSize="md" py={2} truncate maxW="sm">
                    {currentUser?.email}
                  </Text>
                )}
              </Field>
            )}
          </form.Field>
          <Flex mt={4} gap={3}>
            <Button
              variant="solid"
              onClick={toggleEditMode}
              type={editMode ? "button" : "submit"}
              loading={editMode ? form.state.isSubmitting : false}
              disabled={
                editMode
                  ? !form.state.isDirty || !form.state.values.email
                  : false
              }
            >
              {editMode ? "Save" : "Edit"}
            </Button>
            {editMode && (
              <Button
                variant="subtle"
                colorPalette="gray"
                onClick={onCancel}
                disabled={form.state.isSubmitting}
              >
                Cancel
              </Button>
            )}
          </Flex>
        </Box>
      </Container>
    </>
  );
};

export default UserInformation;
