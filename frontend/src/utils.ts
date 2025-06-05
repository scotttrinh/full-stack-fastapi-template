import { StandardSchemaV1Issue } from "@tanstack/react-form";
import { z } from "zod/v4-mini";

import type { ApiError } from "./client";
import useCustomToast from "./hooks/useCustomToast";

const ApiErrorSchema = z.object({
  detail: z.optional(
    z.union([
      z.string(),
      z.pipe(
        z.array(z.object({ msg: z.string() })),
        z.transform((data) => data.map((item) => item.msg).join(", ")),
      ),
    ]),
  ),
});

export const handleError = (err: ApiError) => {
  const { showErrorToast } = useCustomToast();
  const result = ApiErrorSchema.safeParse(err.body);

  showErrorToast(result.data?.detail ?? "Something went wrong.");
};

export const formatErrors = (
  errors: (string | StandardSchemaV1Issue | undefined)[],
): string => {
  return errors
    .map((error) => {
      if (!error) return "";
      if (typeof error === "string") {
        return error;
      }

      return error.message;
    })
    .join(", ");
};
