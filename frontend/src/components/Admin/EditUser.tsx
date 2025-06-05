import { useMutation, useQueryClient } from "@tanstack/react-query";
import { useForm } from "@tanstack/react-form";
import { z } from "zod/v4-mini";

import {
  Button,
  DialogActionTrigger,
  DialogRoot,
  DialogTrigger,
  Flex,
  Input,
  Text,
  VStack,
} from "@chakra-ui/react";
import { useState } from "react";
import { FaExchangeAlt } from "react-icons/fa";

import { type UserPublic, type UserUpdate, UsersService } from "@/client";
import type { ApiError } from "@/client/core/ApiError";
import useCustomToast from "@/hooks/useCustomToast";
import { emailPattern, handleError, PasswordConfirmation } from "@/utils";
import { Checkbox } from "../ui/checkbox";
import {
  DialogBody,
  DialogCloseTrigger,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "../ui/dialog";
import { Field } from "../ui/field";

interface EditUserProps {
  user: UserUpdateForm;
}

/*
export type UserUpdate = {
  email?: string | null
  is_active?: boolean
  is_superuser?: boolean
  full_name?: string | null
  password?: string | null
}
*/
const UserUpdateForm = z.intersection(
  z.intersection(
    z.partial(
      z.object({
        email: z.string().check(z.email()),
        is_active: z.boolean(),
        is_superuser: z.boolean(),
        full_name: z.string(),
      })
    ),
    z.object({
      id: z.string(),
    })
  ),
  PasswordConfirmation
);
type UserUpdateForm = z.output<typeof UserUpdateForm>;

const EditUser = ({ user }: EditUserProps) => {
  const [isOpen, setIsOpen] = useState(false);
  const queryClient = useQueryClient();
  const { showSuccessToast } = useCustomToast();
  const form = useForm({
    validators: {
      onSubmit: UserUpdateForm,
    },
    defaultValues: user,
    onSubmit: (data) => {
      if (data.value.password === "") {
        data.value.password = undefined;
      }
      mutation.mutate(data.value);
    },
  });

  const mutation = useMutation({
    mutationFn: (data: UserUpdateForm) =>
      UsersService.updateUser({ userId: user.id, requestBody: data }),
    onSuccess: () => {
      showSuccessToast("User updated successfully.");
      form.reset();
      setIsOpen(false);
    },
    onError: (err: ApiError) => {
      handleError(err);
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["users"] });
    },
  });

  return (
    <DialogRoot
      size={{ base: "xs", md: "md" }}
      placement="center"
      open={isOpen}
      onOpenChange={({ open }) => setIsOpen(open)}
    >
      <DialogTrigger asChild>
        <Button variant="ghost" size="sm">
          <FaExchangeAlt fontSize="16px" />
          Edit User
        </Button>
      </DialogTrigger>
      <DialogContent>
        <form onSubmit={form.handleSubmit}>
          <DialogHeader>
            <DialogTitle>Edit User</DialogTitle>
          </DialogHeader>
          <DialogBody>
            <Text mb={4}>Update the user details below.</Text>
            <VStack gap={4}>
              <form.Field
                name="email"
                validators={{
                  onChange: ({ value }) => {
                    if (!value) return "Email is required";
                    if (!emailPattern.value.test(value))
                      return emailPattern.message;
                    return undefined;
                  },
                }}
              >
                {(field) => (
                  <Field
                    required
                    invalid={!field.state.meta.isValid}
                    errorText={field.state.meta.errors.join(", ")}
                    label="Email"
                  >
                    <Input
                      id="email"
                      value={field.state.value ?? undefined}
                      onChange={(e) => field.handleChange(e.target.value)}
                      placeholder="Email"
                      type="email"
                    />
                  </Field>
                )}
              </form.Field>

              <form.Field name="full_name">
                {(field) => (
                  <Field
                    invalid={!field.state.meta.isValid}
                    errorText={field.state.meta.errors.join(", ")}
                    label="Full Name"
                  >
                    <Input
                      id="name"
                      value={field.state.value ?? undefined}
                      onChange={(e) => field.handleChange(e.target.value)}
                      placeholder="Full name"
                      type="text"
                    />
                  </Field>
                )}
              </form.Field>

              <form.Field
                name="password"
                validators={{
                  onChange: ({ value }) => {
                    if (value && value.length < 8)
                      return "Password must be at least 8 characters";
                    return undefined;
                  },
                }}
              >
                {(field) => (
                  <Field
                    invalid={!field.state.meta.isValid}
                    errorText={field.state.meta.errors.join(", ")}
                    label="Set Password"
                  >
                    <Input
                      id="password"
                      value={field.state.value ?? undefined}
                      onChange={(e) => field.handleChange(e.target.value)}
                      placeholder="Password"
                      type="password"
                    />
                  </Field>
                )}
              </form.Field>

              <form.Field
                name="confirm_password"
                validators={{
                  onChange: ({ value }) => {
                    if (value && value !== form.getFieldValue("password"))
                      return "The passwords do not match";
                    return undefined;
                  },
                }}
              >
                {(field) => (
                  <Field
                    invalid={!field.state.meta.isValid}
                    errorText={field.state.meta.errors.join(", ")}
                    label="Confirm Password"
                  >
                    <Input
                      id="confirm_password"
                      value={field.state.value}
                      onChange={(e) => field.handleChange(e.target.value)}
                      placeholder="Password"
                      type="password"
                    />
                  </Field>
                )}
              </form.Field>
            </VStack>

            <Flex mt={4} direction="column" gap={4}>
              <form.Field name="is_superuser">
                {(field) => (
                  <Field colorPalette="teal">
                    <Checkbox
                      checked={field.state.value}
                      onCheckedChange={({ checked }) =>
                        field.handleChange(checked === true)
                      }
                    >
                      Is superuser?
                    </Checkbox>
                  </Field>
                )}
              </form.Field>
              <form.Field name="is_active">
                {(field) => (
                  <Field colorPalette="teal">
                    <Checkbox
                      checked={field.state.value}
                      onCheckedChange={({ checked }) =>
                        field.handleChange(checked === true)
                      }
                    >
                      Is active?
                    </Checkbox>
                  </Field>
                )}
              </form.Field>
            </Flex>
          </DialogBody>

          <DialogFooter gap={2}>
            <DialogActionTrigger asChild>
              <Button
                variant="subtle"
                colorPalette="gray"
                disabled={form.state.isSubmitting}
              >
                Cancel
              </Button>
            </DialogActionTrigger>
            <Button
              variant="solid"
              type="submit"
              disabled={!form.state.isValid}
              loading={form.state.isSubmitting}
            >
              Save
            </Button>
          </DialogFooter>
          <DialogCloseTrigger />
        </form>
      </DialogContent>
    </DialogRoot>
  );
};

export default EditUser;
