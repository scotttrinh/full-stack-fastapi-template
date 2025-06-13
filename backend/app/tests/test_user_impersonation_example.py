from fastapi.testclient import TestClient

from app.tests.conftest import TestUsers


def test_healthcheck(client: TestClient):
    response = client.get("/api/v1/utils/health-check")
    assert response.status_code == 200
    assert response.json() is True


def test_user_impersonation_http_requests(test_users: TestUsers):
    """Example of making HTTP requests as different users."""

    # Make a request as superuser1
    response = test_users.superuser1.request.get("/api/v1/users/me")
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["email"] == "superuser1@example.com"
    assert user_data["is_superuser"] is True

    # Make a request as regular user1
    response = test_users.user1.request.get("/api/v1/users/me")
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["email"] == "user1@example.com"
    assert user_data["is_superuser"] is False

    # Create an item as user1
    item_data = {"title": "Test Item", "description": "This is a test item"}
    response = test_users.user1.request.post("/api/v1/items/", json=item_data)
    assert response.status_code == 200
    created_item = response.json()
    assert created_item["title"] == "Test Item"

    # Try to access the item as user2 (should not be allowed due to ownership)
    item_id = created_item["id"]
    response = test_users.user2.request.get(f"/api/v1/items/{item_id}")
    # This will depend on your access control policies


def test_user_impersonation_database_queries(test_users: TestUsers):
    """Example of making database queries as different users using the .db property."""

    # Query as superuser1 (should have full access)
    users = test_users.superuser1.db.query("select User { email, is_superuser }")
    assert len(users) >= 4  # At least our 4 test users

    # Query as regular user1 (may have limited access depending on policies)
    current_user = test_users.user1.db.query_single(
        "select global current_user { email, is_superuser }"
    )
    assert current_user.email == "user1@example.com"
    assert current_user.is_superuser is False

    # Create an item via database as user1
    test_users.user1.db.execute(
        """
        insert Item {
            title := "Database Item",
            description := "Created via database query",
            owner := global current_user
        }
    """
    )

    # Query the item back
    items = test_users.user1.db.query(
        "select Item { title, description } filter .owner = global current_user"
    )
    assert any(item.title == "Database Item" for item in items)


def test_using_get_user_method(test_users: TestUsers):
    """Example of using the get_user method for dynamic user selection."""

    user_types = ["superuser1", "user1", "user2"]

    for user_type in user_types:
        user = test_users.get_user(user_type)
        response = user.request.get("/api/v1/users/me")
        assert response.status_code == 200

        user_data = response.json()
        expected_email = f"{user_type}@example.com"
        assert user_data["email"] == expected_email


def test_mixed_http_and_database_operations(test_users: TestUsers):
    """Example of combining HTTP requests and database queries."""

    # Create an item via HTTP API as user1
    item_data = {
        "title": "Mixed Test Item",
        "description": "Created via HTTP, verified via DB",
    }
    response = test_users.user1.request.post("/api/v1/items/", json=item_data)
    assert response.status_code == 200
    created_item = response.json()

    # Verify the item exists in the database as user1
    db_items = test_users.user1.db.query(
        """
        select Item { 
            title, 
            description, 
            owner: { email } 
        } 
        filter .title = "Mixed Test Item"
    """
    )

    assert len(db_items) == 1
    assert db_items[0].title == "Mixed Test Item"
    assert db_items[0].owner.email == "user1@example.com"

    # Verify superuser can see all items
    all_items = test_users.superuser1.db.query("select Item { title }")
    item_titles = [item.title for item in all_items]
    assert "Mixed Test Item" in item_titles


def test_access_control_between_users(test_users: TestUsers):
    """Example of testing access control between different users."""

    # User1 creates an item
    item_data = {
        "title": "User1's Private Item",
        "description": "Should only be accessible to user1",
    }
    response = test_users.user1.request.post("/api/v1/items/", json=item_data)
    assert response.status_code == 200
    created_item = response.json()
    item_id = created_item["id"]

    # User1 can access their own item
    response = test_users.user1.request.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200

    # User2 cannot access user1's item (depending on your access policies)
    response = test_users.user2.request.get(f"/api/v1/items/{item_id}")
    # The exact status code will depend on your access control implementation
    # This is just an example of how you'd test it

    # Superuser can access any item
    response = test_users.superuser1.request.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200


def test_direct_database_client_access(test_users: TestUsers):
    """Example showing direct access to the impersonated database client."""

    # Each user has their own impersonated database client
    user1_db = test_users.user1.db
    user2_db = test_users.user2.db
    superuser_db = test_users.superuser1.db

    # Current user should be different for each client
    user1_current = user1_db.query_single("select global current_user { email }")
    user2_current = user2_db.query_single("select global current_user { email }")

    assert user1_current.email == "user1@example.com"
    assert user2_current.email == "user2@example.com"

    # Superuser should see all users
    all_users = superuser_db.query("select User { email } order by .email")
    emails = [user.email for user in all_users]
    assert "superuser1@example.com" in emails
    assert "user1@example.com" in emails
    assert "user2@example.com" in emails

    # Regular user queries are subject to access policies
    user1_visible_users = user1_db.query("select User { email }")
    # The results here depend on your access control policies
