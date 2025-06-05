import { useMutation, useQueryClient } from "@tanstack/react-query"
import { useForm } from "@tanstack/react-form"

import { type UserCreate, UsersService } from "@/client"
import type { ApiError } from "@/client/core/ApiError"
import useCustomToast from "@/hooks/useCustomToast"
import { emailPattern, handleError } from "@/utils"
import {
  Button,
  DialogActionTrigger,
  DialogTitle,
  Flex,
  Input,
  Text,
  VStack,
} from "@chakra-ui/react"
import { useState } from "react"
import { FaPlus } from "react-icons/fa"
import { Checkbox } from "../ui/checkbox"
import {
  DialogBody,
  DialogCloseTrigger,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogRoot,
  DialogTrigger,
} from "../ui/dialog"
import { Field } from "../ui/field"

interface UserCreateForm extends UserCreate {
  confirm_password: string
}

const AddUser = () => {
  const [isOpen, setIsOpen] = useState(false)
  const queryClient = useQueryClient()
  const { showSuccessToast } = useCustomToast()
  const form = useForm({
    defaultValues: {
      email: "",
      full_name: "",
      password: "",
      confirm_password: "",
      is_superuser: false,
      is_active: false,
    } as UserCreateForm,
    onSubmit: (data) => {
      mutation.mutate(data.value);
    },
  });

  const mutation = useMutation({
    mutationFn: (data: UserCreate) =>
      UsersService.createUser({ requestBody: data }),
    onSuccess: () => {
      showSuccessToast("User created successfully.")
      form.reset()
      setIsOpen(false)
    },
    onError: (err: ApiError) => {
      handleError(err)
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["users"] })
    },
  })

  return (
    <DialogRoot
      size={{ base: "xs", md: "md" }}
      placement="center"
      open={isOpen}
      onOpenChange={({ open }) => setIsOpen(open)}
    >
      <DialogTrigger asChild>
        <Button value="add-user" my={4}>
          <FaPlus fontSize="16px" />
          Add User
        </Button>
      </DialogTrigger>
      <DialogContent>
        <form onSubmit={form.handleSubmit}>
          <DialogHeader>
            <DialogTitle>Add User</DialogTitle>
          </DialogHeader>
          <DialogBody>
            <Text mb={4}>
              Fill in the form below to add a new user to the system.
            </Text>
            <VStack gap={4}>
              <form.Field
                name="email"
                validators={{
                  onChange: ({ value }) => {
                    if (!value) return "Email is required";
                    if (!emailPattern.value.test(value)) return emailPattern.message;
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
                      value={field.state.value}
                      onChange={(e) => field.handleChange(e.target.value)}
                      placeholder="Email"
                      type="email"
                    />
                  </Field>
                )}
              </form.Field>

              <form.Field
                name="full_name"
              >
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
                    if (!value) return "Password is required";
                    if (value.length < 8) return "Password must be at least 8 characters";
                    return undefined;
                  },
                }}
              >
                {(field) => (
                  <Field
                    required
                    invalid={!field.state.meta.isValid}
                    errorText={field.state.meta.errors.join(", ")}
                    label="Set Password"
                  >
                    <Input
                      id="password"
                      value={field.state.value}
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
                    if (!value) return "Please confirm your password";
                    if (value !== form.getFieldValue("password")) return "The passwords do not match";
                    return undefined;
                  },
                }}
              >
                {(field) => (
                  <Field
                    required
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
              <form.Field
                name="is_superuser"
              >
                {(field) => (
                  <Field colorPalette="teal">
                    <Checkbox
                      checked={field.state.value}
                      onCheckedChange={({ checked }) => field.handleChange(checked === true)}
                    >
                      Is superuser?
                    </Checkbox>
                  </Field>
                )}
              </form.Field>
              <form.Field
                name="is_active"
              >
                {(field) => (
                  <Field colorPalette="teal">
                    <Checkbox
                      checked={field.state.value}
                      onCheckedChange={({ checked }) => field.handleChange(checked === true)}
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
        </form>
        <DialogCloseTrigger />
      </DialogContent>
    </DialogRoot>
  )
}

export default AddUser
