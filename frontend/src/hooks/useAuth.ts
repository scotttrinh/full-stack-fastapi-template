import { useQuery, useQueryClient, useMutation } from "@tanstack/react-query";
import { useCallback } from "react";
import { z } from "zod/v4";

import { type User, UsersService } from "@/client";

const UnauthorizedApiError = z.object({
  status: z.literal(401),
});

export const useAuth = () => {
  const queryClient = useQueryClient();

  const {
    data: user,
    error,
    refetch,
  } = useQuery<User | null, Error>({
    queryKey: ["currentUser"],
    queryFn: async () => {
      try {
        return await UsersService.readUserMe();
      } catch (err) {
        if (UnauthorizedApiError.safeParse(err).success) {
          return null;
        }
        throw err;
      }
    },
    retry: (failureCount, error) => {
      if (UnauthorizedApiError.safeParse(error).success) {
        return false;
      }
      return failureCount < 3;
    },
    refetchInterval: 10 * 60 * 1000,
  });

  const logoutMutation = useMutation({
    mutationFn: async () => {
      return await fetch("/auth/sign-out", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      });
    },
    onSuccess: () => {
      queryClient.setQueryData(["currentUser"], null);
    },
    onError: (error) => {
      console.error("Logout failed:", error);
    },
  });

  const invalidateUser = useCallback(async () => {
    await queryClient.invalidateQueries({ queryKey: ["currentUser"] });
  }, [queryClient]);

  const login = useCallback(() => {
    window.location.href = "/auth/sign-in";
  }, []);

  const register = useCallback(() => {
    window.location.href = "/auth/sign-up";
  }, []);

  const logout = useCallback(async () => {
    await logoutMutation.mutateAsync();
    window.location.href = "/auth/sign-in";
  }, [logoutMutation]);

  return {
    user,
    error,
    isLoggedIn: user !== null,
    isLoading: user === undefined,
    login,
    register,
    logout,
    refetch,
    invalidateUser,
  };
};

export default useAuth;
