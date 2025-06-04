import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useNavigate } from "@tanstack/react-router";
import { useState } from "react";

import {
  type ApiError,
  type UserPublic,
  type UserRegister,
  UsersService,
} from "@/client";
import { handleError } from "@/utils";

export const useAuth = () => {
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();
  const queryClient = useQueryClient();
  const { data: user } = useQuery<UserPublic | null, Error>({
    queryKey: ["currentUser"],
    queryFn: () => UsersService.readUserMe(),
  });

  const signUpMutation = useMutation({
    mutationFn: (data: UserRegister) =>
      UsersService.registerUser({ requestBody: data }),

    onSuccess: () => {
      void navigate({ to: "/" });
    },
    onError: (err: ApiError) => {
      handleError(err);
    },
    onSettled: async () => {
      await queryClient.invalidateQueries({ queryKey: ["users"] });
    },
  });

  const login = async () => {
    await navigate({
      href: new URL("/api/v1/auth/login", window.location.origin).href,
      reloadDocument: true,
    });
  };

  const loginMutation = useMutation({
    mutationFn: login,
    onError: (err: ApiError) => {
      handleError(err);
    },
  });

  const logout = async () => {
    await navigate({
      href: new URL("/api/v1/auth/logout", window.location.origin).href,
      reloadDocument: true,
    });
  };

  return {
    signUpMutation,
    loginMutation,
    logout,
    user,
    error,
    resetError: () => setError(null),
    isLoggedIn: user !== null,
  };
};

export default useAuth;
