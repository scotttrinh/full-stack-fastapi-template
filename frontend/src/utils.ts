import { FieldValidateFn, FormValidateFn } from "@tanstack/react-form";
import type { ApiError } from "./client";
import useCustomToast from "./hooks/useCustomToast";
import { z } from "zod/v4-mini";

export const emailPattern = {
  value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
  message: "Invalid email address",
};

export const namePattern = {
  value: /^[A-Za-z\s\u00C0-\u017F]{1,30}$/,
  message: "Invalid name",
};

export const Email = z
  .string()
  .check(z.email({ message: "Invalid email address" }));

export const Password = z
  .string()
  .check(z.minLength(8, "Password must be at least 8 characters"));

export const PasswordConfirmation = z
  .object({
    password: z.optional(Password),
    new_password: z.optional(Password),
    confirm_password: z.string(),
  })
  .check(
    z.refine((data) => {
      const password = data.password ?? data.new_password;
      if (password && data.confirm_password !== password) {
        return "The passwords do not match";
      }
      return true;
    })
  );

export const handleError = (err: ApiError) => {
  const { showErrorToast } = useCustomToast();
  const errDetail = (err.body as any)?.detail;
  let errorMessage = errDetail || "Something went wrong.";
  if (Array.isArray(errDetail) && errDetail.length > 0) {
    errorMessage = errDetail[0].msg;
  }
  showErrorToast(errorMessage);
};
