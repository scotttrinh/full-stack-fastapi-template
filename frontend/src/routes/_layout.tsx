import { Flex } from "@chakra-ui/react";
import { Outlet, createFileRoute } from "@tanstack/react-router";

import Navbar from "@/components/Common/Navbar";
import Sidebar from "@/components/Common/Sidebar";
import { useAuth } from "@/hooks/useAuth";

export const Route = createFileRoute("/_layout")({
  component: Layout,
});

function Layout() {
  const { isLoggedIn, loginMutation } = useAuth();

  if (!isLoggedIn) {
    return loginMutation.mutate();
  }

  return (
    <Flex direction="column" h="100vh">
      <Navbar />
      <Flex flex="1" overflow="hidden">
        <Sidebar />
        <Flex flex="1" direction="column" p={4} overflowY="auto">
          <Outlet />
        </Flex>
      </Flex>
    </Flex>
  );
}

export default Layout;
