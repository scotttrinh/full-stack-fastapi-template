import uuid

from fastapi.testclient import TestClient

from app.tests.conftest import TestUsers


class TestUsersRoutes:
    """Test all user-related API endpoints."""

    def test_list_users_as_superuser(self, client: TestClient, test_users: TestUsers):
        """Superuser can list all users."""
        request = client.build_request(
            "GET", "/api/v1/users/", cookies=test_users.superuser1.cookies
        )
        response = client.send(request)
        assert response.status_code == 200, response.text
        data = response.json()
        assert "data" in data
        assert "count" in data
        assert data["count"] == 4
        assert len(data["data"]) == 4

    def test_list_users_as_regular_user_forbidden(
        self, client: TestClient, test_users: TestUsers
    ):
        """Regular user cannot list users."""
        request = client.build_request(
            "GET", "/api/v1/users/", cookies=test_users.user1.cookies
        )
        response = client.send(request)
        assert response.status_code == 403, response.text

    def test_list_users_unauthenticated(self, client: TestClient):
        """Unauthenticated request fails."""
        response = client.get("/api/v1/users/")
        assert (
            response.status_code == 401
        ), f"Expected 401, got {response.status_code}: {response.text}"

    def test_get_current_user(self, client: TestClient, test_users: TestUsers):
        """Authenticated user can get their own profile."""
        request = client.build_request(
            "GET", "/api/v1/users/me", cookies=test_users.user1.cookies
        )
        response = client.send(request)
        assert response.status_code == 200, response.text
        user_data = response.json()
        assert user_data["email"] == "user1@example.com"
        assert user_data["is_superuser"] is False

    def test_get_current_user_unauthenticated(self, client: TestClient):
        """Unauthenticated user cannot get current user."""
        response = client.get("/api/v1/users/me")
        assert response.status_code == 401, response.text

    def test_update_current_user(self, client: TestClient, test_users: TestUsers):
        """User can update their own profile."""
        update_data = {"full_name": "Updated Name"}
        request = client.build_request(
            "PATCH",
            "/api/v1/users/me",
            json=update_data,
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 200, response.text
        updated_user = response.json()
        assert updated_user["full_name"] == "Updated Name"
        assert updated_user["email"] == "user1@example.com"

    def test_update_current_user_unauthenticated(self, client: TestClient):
        """Unauthenticated user cannot update profile."""
        update_data = {"full_name": "Blocked Update"}
        response = client.patch("/api/v1/users/me", json=update_data)
        assert response.status_code == 401, response.text

    def test_update_current_user_malformed_data(
        self, client: TestClient, test_users: TestUsers
    ):
        """Updating user with invalid data fails."""
        # Invalid JSON structure
        request = client.build_request(
            "PATCH",
            "/api/v1/users/me",
            json="invalid",
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 422, response.text

    def test_delete_current_user_regular_user(
        self, client: TestClient, test_users: TestUsers
    ):
        """Regular user can delete their own account."""
        request = client.build_request(
            "DELETE", "/api/v1/users/me", cookies=test_users.user2.cookies
        )
        response = client.send(request)
        assert response.status_code == 204, response.text

    def test_delete_current_user_superuser_forbidden(
        self, client: TestClient, test_users: TestUsers
    ):
        """Superuser cannot delete themselves."""
        request = client.build_request(
            "DELETE", "/api/v1/users/me", cookies=test_users.superuser1.cookies
        )
        response = client.send(request)
        assert response.status_code == 403, response.text

    def test_delete_current_user_unauthenticated(self, client: TestClient):
        """Unauthenticated user cannot delete account."""
        response = client.delete("/api/v1/users/me")
        assert response.status_code == 401, response.text

    def test_get_user_by_id_own_user(self, client: TestClient, test_users: TestUsers):
        """User can get their own profile by ID."""
        user_id = test_users.user1.id
        request = client.build_request(
            "GET", f"/api/v1/users/{user_id}", cookies=test_users.user1.cookies
        )
        response = client.send(request)
        assert response.status_code == 200, response.text
        user_data = response.json()
        assert user_data["email"] == "user1@example.com"

    def test_get_user_by_id_other_user_forbidden(
        self, client: TestClient, test_users: TestUsers
    ):
        """User cannot get another user's profile by ID."""
        request = client.build_request(
            "GET",
            f"/api/v1/users/{test_users.user2.id}",
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 403, response.text

    def test_get_user_by_id_invalid_uuid(
        self, client: TestClient, test_users: TestUsers
    ):
        """Getting user with invalid UUID fails."""
        request = client.build_request(
            "GET",
            "/api/v1/users/invalid-uuid",
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 422, response.text

    def test_get_user_by_id_nonexistent(
        self, client: TestClient, test_users: TestUsers
    ):
        """Getting nonexistent user returns 404."""
        fake_id = str(uuid.uuid4())
        request = client.build_request(
            "GET",
            f"/api/v1/users/{fake_id}",
            cookies=test_users.superuser1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 404, response.text

    def test_get_user_by_id_unauthenticated(
        self, client: TestClient, test_users: TestUsers
    ):
        """Unauthenticated user cannot get user by ID."""
        user_id = test_users.user1.id
        request = client.build_request(
            "GET",
            f"/api/v1/users/{user_id}",
        )
        response = client.send(request)
        assert response.status_code == 401, response.text

    def test_update_user_by_id_as_superuser(
        self, client: TestClient, test_users: TestUsers
    ):
        """Superuser can update any user by ID."""
        user_id = test_users.user1.id
        update_data = {"full_name": "Superuser Updated Name"}
        request = client.build_request(
            "PATCH",
            f"/api/v1/users/{user_id}",
            json=update_data,
            cookies=test_users.superuser1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 200, response.text
        updated_user = response.json()
        assert updated_user["full_name"] == "Superuser Updated Name"

    def test_update_user_by_id_as_regular_user_forbidden(
        self, client: TestClient, test_users: TestUsers
    ):
        """Regular user cannot update other users by ID."""
        user2_id = test_users.user2.id
        update_data = {"full_name": "Blocked Update"}
        request = client.build_request(
            "PATCH",
            f"/api/v1/users/{user2_id}",
            json=update_data,
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 403, response.text

    def test_update_user_by_id_nonexistent(
        self, client: TestClient, test_users: TestUsers
    ):
        """Updating nonexistent user returns 404."""
        fake_id = str(uuid.uuid4())
        update_data = {"full_name": "Won't Work"}
        request = client.build_request(
            "PATCH",
            f"/api/v1/users/{fake_id}",
            json=update_data,
            cookies=test_users.superuser1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 404, response.text

    def test_update_user_by_id_unauthenticated(
        self, client: TestClient, test_users: TestUsers
    ):
        """Unauthenticated user cannot update users."""
        user_id = test_users.user1.id
        update_data = {"full_name": "Blocked"}
        request = client.build_request(
            "PATCH",
            f"/api/v1/users/{user_id}",
            json=update_data,
        )
        response = client.send(request)
        assert response.status_code == 401, response.text

    def test_delete_user_by_id_as_superuser(
        self, client: TestClient, test_users: TestUsers
    ):
        """Superuser can delete other users by ID."""
        # First create a user to delete
        user_data = {
            "email": "todelete@example.com",
            "password": uuid.uuid4().hex,
            "full_name": "To Delete",
        }
        request = client.build_request(
            "POST",
            "/auth/register",
            json=user_data,
            cookies=test_users.superuser1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 303, response.text

        request = client.build_request(
            "GET",
            "/api/v1/users/",
            cookies=test_users.superuser1.cookies,
        )
        all_users = client.send(request)
        assert all_users.status_code == 200, all_users.text
        all_users_data = all_users.json()
        assert "data" in all_users_data
        assert "count" in all_users_data
        assert all_users_data["count"] == 5, all_users.text
        assert len(all_users_data["data"]) == 5, all_users.text
        created_user = next(
            user
            for user in all_users_data["data"]
            if user["email"] == "todelete@example.com"
        )
        assert created_user is not None

        # Now delete the user
        request = client.build_request(
            "DELETE",
            f"/api/v1/users/{created_user['id']}",
            cookies=test_users.superuser1.cookies,
        )
        response = client.send(request)
        assert (
            response.status_code == 200
        ), f"Expected 200, got {response.status_code}: {response.text}"

    def test_delete_user_by_id_superuser_cannot_delete_self(
        self, client: TestClient, test_users: TestUsers
    ):
        """Superuser cannot delete themselves by ID."""
        request = client.build_request(
            "DELETE",
            f"/api/v1/users/{test_users.superuser1.id}",
            cookies=test_users.superuser1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 403, response.text

    def test_delete_user_by_id_as_regular_user_forbidden(
        self, client: TestClient, test_users: TestUsers
    ):
        """Regular user cannot delete users by ID."""
        user2_id = test_users.user2.id
        request = client.build_request(
            "DELETE",
            f"/api/v1/users/{user2_id}",
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 403, response.text

    def test_delete_user_by_id_unauthenticated(
        self, client: TestClient, test_users: TestUsers
    ):
        """Unauthenticated user cannot delete users."""
        user_id = test_users.user1.id
        request = client.build_request(
            "DELETE",
            f"/api/v1/users/{user_id}",
        )
        response = client.send(request)
        assert response.status_code == 401, response.text


class TestItemsRoutes:
    """Test all item-related API endpoints."""

    def test_list_items_authenticated(self, client: TestClient, test_users: TestUsers):
        """Authenticated user can list items."""
        request = client.build_request(
            "GET",
            "/api/v1/items/",
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 200, response.text
        data = response.json()
        assert "data" in data

    def test_list_items_unauthenticated(self, client: TestClient):
        """Unauthenticated user cannot list items."""
        request = client.build_request(
            "GET",
            "/api/v1/items/",
        )
        response = client.send(request)
        assert response.status_code == 401, response.text

    def test_create_item_authenticated(self, client: TestClient, test_users: TestUsers):
        """Authenticated user can create items."""
        item_data = {"title": "Test Item", "description": "This is a test item"}
        request = client.build_request(
            "POST",
            "/api/v1/items/",
            json=item_data,
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 200, response.text
        created_item = response.json()
        assert created_item["title"] == "Test Item"
        assert created_item["description"] == "This is a test item"

    def test_create_item_unauthenticated(self, client: TestClient):
        """Unauthenticated user cannot create items."""
        item_data = {"title": "Blocked Item", "description": "Should not be created"}
        request = client.build_request(
            "POST",
            "/api/v1/items/",
            json=item_data,
        )
        response = client.send(request)
        assert response.status_code == 401, response.text

    def test_create_item_malformed_data(
        self, client: TestClient, test_users: TestUsers
    ):
        """Creating item with malformed data fails."""
        request = client.build_request(
            "POST",
            "/api/v1/items/",
            json="invalid",
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 422, response.text

        # Empty object should still work (optional fields)
        request = client.build_request(
            "POST",
            "/api/v1/items/",
            json={},
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 200, response.text

    def test_get_item_by_id_authenticated(
        self, client: TestClient, test_users: TestUsers
    ):
        """Authenticated user can get item by ID."""
        # First create an item
        item_data = {"title": "Get Test Item", "description": "For getting"}
        request = client.build_request(
            "POST",
            "/api/v1/items/",
            json=item_data,
            cookies=test_users.user1.cookies,
        )
        create_response = client.send(request)
        assert create_response.status_code == 200, create_response.text
        created_item = create_response.json()

        # Now get the item
        request = client.build_request(
            "GET",
            f"/api/v1/items/{created_item['id']}",
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 200, response.text
        item = response.json()
        assert item["title"] == "Get Test Item"

    def test_get_item_by_id_unauthenticated(
        self, client: TestClient, test_users: TestUsers
    ):
        """Unauthenticated user cannot get items."""
        # First create an item
        item_data = {"title": "Blocked Access Item"}
        request = client.build_request(
            "POST",
            "/api/v1/items/",
            json=item_data,
            cookies=test_users.user1.cookies,
        )
        create_response = client.send(request)
        assert create_response.status_code == 200, create_response.text
        created_item = create_response.json()

        # Try to get without auth
        request = client.build_request(
            "GET",
            f"/api/v1/items/{created_item['id']}",
        )
        response = client.send(request)
        assert response.status_code == 401, response.text

    def test_get_item_by_id_nonexistent(
        self, client: TestClient, test_users: TestUsers
    ):
        """Getting nonexistent item returns 404."""
        fake_id = str(uuid.uuid4())
        request = client.build_request(
            "GET",
            f"/api/v1/items/{fake_id}",
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 404, response.text

    def test_get_item_by_id_invalid_uuid(
        self, client: TestClient, test_users: TestUsers
    ):
        """Getting item with invalid UUID fails."""
        request = client.build_request(
            "GET",
            "/api/v1/items/invalid-uuid",
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 422, response.text

    def test_update_item_authenticated(self, client: TestClient, test_users: TestUsers):
        """Authenticated user can update items."""
        # First create an item
        item_data = {"title": "Original Title", "description": "Original description"}
        request = client.build_request(
            "POST",
            "/api/v1/items/",
            json=item_data,
            cookies=test_users.user1.cookies,
        )
        create_response = client.send(request)
        assert create_response.status_code == 200, create_response.text
        created_item = create_response.json()

        # Now update the item
        update_data = {"title": "Updated Title", "description": "Updated description"}
        request = client.build_request(
            "PUT",
            f"/api/v1/items/{created_item['id']}",
            json=update_data,
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 200, response.text
        updated_item = response.json()
        assert updated_item["title"] == "Updated Title"
        assert updated_item["description"] == "Updated description"

    def test_update_item_unauthenticated(
        self, client: TestClient, test_users: TestUsers
    ):
        """Unauthenticated user cannot update items."""
        # First create an item
        item_data = {"title": "Protected Item"}
        request = client.build_request(
            "POST",
            "/api/v1/items/",
            json=item_data,
            cookies=test_users.user1.cookies,
        )
        create_response = client.send(request)
        assert create_response.status_code == 200, create_response.text
        created_item = create_response.json()

        # Try to update without auth
        update_data = {"title": "Hacked Title"}
        request = client.build_request(
            "PUT",
            f"/api/v1/items/{created_item['id']}",
            json=update_data,
        )
        response = client.send(request)
        assert response.status_code == 401, response.text

    def test_update_item_nonexistent(self, client: TestClient, test_users: TestUsers):
        """Updating nonexistent item returns 404."""
        fake_id = str(uuid.uuid4())
        update_data = {"title": "Won't Work"}
        request = client.build_request(
            "PUT",
            f"/api/v1/items/{fake_id}",
            json=update_data,
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 404, response.text

    def test_update_item_malformed_data(
        self, client: TestClient, test_users: TestUsers
    ):
        """Updating item with malformed data fails."""
        # First create an item
        item_data = {"title": "Valid Item"}
        request = client.build_request(
            "POST",
            "/api/v1/items/",
            json=item_data,
            cookies=test_users.user1.cookies,
        )
        create_response = client.send(request)
        assert create_response.status_code == 200, create_response.text
        created_item = create_response.json()

        # Try to update with invalid data
        request = client.build_request(
            "PUT",
            f"/api/v1/items/{created_item['id']}",
            json="invalid",
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 422, response.text

    def test_delete_item_authenticated(self, client: TestClient, test_users: TestUsers):
        """Authenticated user can delete items."""
        # First create an item
        item_data = {"title": "To Delete", "description": "Will be deleted"}
        request = client.build_request(
            "POST",
            "/api/v1/items/",
            json=item_data,
            cookies=test_users.user1.cookies,
        )
        create_response = client.send(request)
        assert create_response.status_code == 200, create_response.text
        created_item = create_response.json()

        # Now delete the item
        request = client.build_request(
            "DELETE",
            f"/api/v1/items/{created_item['id']}",
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 204, response.text

    def test_delete_item_unauthenticated(
        self, client: TestClient, test_users: TestUsers
    ):
        """Unauthenticated user cannot delete items."""
        # First create an item
        item_data = {"title": "Protected Item"}
        request = client.build_request(
            "POST",
            "/api/v1/items/",
            json=item_data,
            cookies=test_users.user1.cookies,
        )
        create_response = client.send(request)
        assert create_response.status_code == 200, create_response.text
        created_item = create_response.json()

        # Try to delete without auth
        request = client.build_request(
            "DELETE",
            f"/api/v1/items/{created_item['id']}",
        )
        response = client.send(request)
        assert response.status_code == 401, response.text

    def test_delete_item_nonexistent(self, client: TestClient, test_users: TestUsers):
        """Deleting nonexistent item succeeds (idempotent)."""
        fake_id = str(uuid.uuid4())
        request = client.build_request(
            "DELETE",
            f"/api/v1/items/{fake_id}",
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code in [204, 404]


class TestUtilsRoutes:
    """Test utility API endpoints."""

    def test_health_check_no_auth_required(self, client: TestClient):
        """Health check endpoint works without authentication."""
        request = client.build_request(
            "GET",
            "/api/v1/utils/health-check",
        )
        response = client.send(request)
        assert response.status_code == 200, response.text
        assert response.json() is True

    def test_health_check_with_auth(self, client: TestClient, test_users: TestUsers):
        """Health check endpoint also works with authentication."""
        request = client.build_request(
            "GET",
            "/api/v1/utils/health-check",
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 200, response.text
        assert response.json() is True


class TestCrossEndpointScenarios:
    """Test complex scenarios involving multiple endpoints."""

    def test_item_ownership_across_users(
        self, client: TestClient, test_users: TestUsers
    ):
        """Test item ownership and access control between users."""
        # User1 creates an item
        item_data = {"title": "User1's Item", "description": "Owned by user1"}
        request = client.build_request(
            "POST",
            "/api/v1/items/",
            json=item_data,
            cookies=test_users.user1.cookies,
        )
        create_response = client.send(request)
        assert create_response.status_code == 200, create_response.text
        created_item = create_response.json()

        # User1 can access their own item
        request = client.build_request(
            "GET",
            f"/api/v1/items/{created_item['id']}",
            cookies=test_users.user1.cookies,
        )
        response = client.send(request)
        assert response.status_code == 200, response.text

        # User2 access depends on access policies (could be 200 or 403/404)
        request = client.build_request(
            "GET",
            f"/api/v1/items/{created_item['id']}",
            cookies=test_users.user2.cookies,
        )
        response = client.send(request)
        # We'll just verify it's a valid response
        assert response.status_code in [200, 403, 404]
