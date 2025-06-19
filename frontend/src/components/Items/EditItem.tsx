import {
  Button,
  ButtonGroup,
  DialogActionTrigger,
  Input,
  Text,
  VStack,
} from "@chakra-ui/react";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { useState } from "react";
import { useForm } from "@tanstack/react-form";
import { FaExchangeAlt } from "react-icons/fa";

import { type ApiError, type Item, type ItemUpdate, ItemsService } from "@/client";
import useCustomToast from "@/hooks/useCustomToast";
import { handleError } from "@/utils";
import {
  DialogBody,
  DialogCloseTrigger,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogRoot,
  DialogTitle,
  DialogTrigger,
} from "../ui/dialog";
import { Field } from "../ui/field";

interface EditItemProps {
  item: Item;
}

interface ItemUpdateForm {
  title?: string | null;
  description?: string | null;
}

const EditItem = ({ item }: EditItemProps) => {
  const [isOpen, setIsOpen] = useState(false);
  const queryClient = useQueryClient();
  const { showSuccessToast } = useCustomToast();
  const form = useForm({
    defaultValues: {
      title: item.title ?? "",
      description: item.description ?? "",
    },
    onSubmit: (data) => {
      mutation.mutate(data.value);
    },
  });

  const mutation = useMutation({
    mutationFn: (data: ItemUpdateForm) =>
      ItemsService.updateItem({ id: item.id, requestBody: data as ItemUpdate }),
    onSuccess: () => {
      showSuccessToast("Item updated successfully.");
      form.reset();
      setIsOpen(false);
    },
    onError: (err: ApiError) => {
      handleError(err);
    },
    onSettled: async () => {
      await queryClient.invalidateQueries({ queryKey: ["items"] });
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
        <Button variant="ghost">
          <FaExchangeAlt fontSize="16px" />
          Edit Item
        </Button>
      </DialogTrigger>
      <DialogContent>
        <form onSubmit={() => void form.handleSubmit()}>
          <DialogHeader>
            <DialogTitle>Edit Item</DialogTitle>
          </DialogHeader>
          <DialogBody>
            <Text mb={4}>Update the item details below.</Text>
            <VStack gap={4}>
              <form.Field
                name="title"
                validators={{
                  onChange: ({ value }) => {
                    if (!value) return "Title is required";
                    return undefined;
                  },
                }}
              >
                {(field) => (
                  <Field
                    required
                    invalid={!field.state.meta.isValid}
                    errorText={field.state.meta.errors.join(", ")}
                    label="Title"
                  >
                    <Input
                      id="title"
                      value={field.state.value ?? ""}
                      onChange={(e) => field.handleChange(e.target.value)}
                      placeholder="Title"
                      type="text"
                    />
                  </Field>
                )}
              </form.Field>

              <form.Field name="description">
                {(field) => (
                  <Field
                    invalid={!field.state.meta.isValid}
                    errorText={field.state.meta.errors.join(", ")}
                    label="Description"
                  >
                    <Input
                      id="description"
                      value={field.state.value ?? ""}
                      onChange={(e) => field.handleChange(e.target.value)}
                      placeholder="Description"
                      type="text"
                    />
                  </Field>
                )}
              </form.Field>
            </VStack>
          </DialogBody>

          <DialogFooter gap={2}>
            <ButtonGroup>
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
                loading={form.state.isSubmitting}
              >
                Save
              </Button>
            </ButtonGroup>
          </DialogFooter>
        </form>
        <DialogCloseTrigger />
      </DialogContent>
    </DialogRoot>
  );
};

export default EditItem;
