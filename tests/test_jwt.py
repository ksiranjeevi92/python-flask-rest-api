import uuid
import unittest

from app import create_app


class JwtTokenTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app("sqlite:///test_jwt.db")
        self.app.testing = True
        self.client = self.app.test_client()

    def test_login_and_access_item_with_bearer_token(self):
        username = f"user-{uuid.uuid4().hex[:8]}"
        password = "secret123"

        register_resp = self.client.post("/register", json={"username": username, "password": password})
        self.assertEqual(register_resp.status_code, 201)

        login_resp = self.client.post("/login", json={"username": username, "password": password})
        self.assertEqual(login_resp.status_code, 200, login_resp.get_data(as_text=True))

        access_token = login_resp.get_json()["access_token"]
        item_resp = self.client.get(
            "/item",
            headers={"Authorization": f"Bearer {access_token}"},
        )

        self.assertEqual(item_resp.status_code, 200, item_resp.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
