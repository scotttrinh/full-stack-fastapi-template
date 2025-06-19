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

import { UsersService } from "@/client";
import type { ApiError } from "@/client/core/ApiError";
import useCustomToast from "@/hooks/useCustomToast";
import { formatErrors, handleError } from "@/utils";
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

const UserUpdateForm = z.intersection(
  z.partial(
    z.object({
      email: z.string().check(z.email()),
      is_superuser: z.boolean(),
      full_name: z.nullable(z.string()),
    }),
  ),
  z.object({
    id: z.string(),
  }),
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
    onSettled: async () => {
      await queryClient.invalidateQueries({ queryKey: ["users"] });
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
        <form onSubmit={() => void form.handleSubmit()}>
          <DialogHeader>
            <DialogTitle>Edit User</DialogTitle>
          </DialogHeader>
          <DialogBody>
            <Text mb={4}>Update the user details below.</Text>
            <VStack gap={4}>
              <form.Field name="email">
                {(field) => (
                  <Field
                    required
                    invalid={!field.state.meta.isValid}
                    errorText={formatErrors(field.state.meta.errors)}
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
                    errorText={formatErrors(field.state.meta.errors)}
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
