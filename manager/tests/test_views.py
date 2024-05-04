from django.test import TestCase
from django.urls import reverse

HTTP_OK = 200
HTTP_FOUND = 302
HTTP_BAD_REQUEST = 400


class ManagerIndexViewTests(TestCase):
    """
    IndexView Tests.

    Methods
    -------
    test_index_view() -> None
        Test if index view returns 200

    """

    def test_index_view(self) -> None:
        """Test if index view returns 200."""
        response = self.client.get(reverse("manager:index"))
        assert response.status_code == HTTP_OK  # noqa: S101


class ManagerEditorViewTests(TestCase):
    """
    IndexView Tests.

    Methods
    -------
    test_create_product_category_view() -> None
        Test if product category editor returns 200

    test_product_category_editor_delete_error_message() -> None
        Test if product category editor error message can be deleted

    test_create_new_product_category() -> None
        Test if new product category can be created

    test_create_new_product_category_empty() -> None
        Test that empty request for product category fails

    test_create_new_product_category_invalid_empty() -> None
        Test that invalid empty request for product category fails

    test_create_new_product_category_invalid_too_long() -> None
        Test that invalid too long request for product category fails

    """

    def test_create_product_category_view(self) -> None:
        """Test if product category editor returns 200."""
        response = self.client.get(reverse("manager:product_category_editor"))
        assert response.status_code == HTTP_OK  # noqa: S101

    def test_product_category_editor_delete_error_message(self) -> None:
        """Test if product category editor error message can be deleted."""
        response = self.client.get(reverse("manager:delete_error_message"))
        assert response.status_code == HTTP_OK  # noqa: S101
        assert response.content == b""  # noqa: S101

    def test_create_new_product_category(self) -> None:
        """Test if new product category can be created."""
        context = {
            "product_category_name": "my_name",
        }

        response = self.client.post(
            reverse("manager:create_new_product_category"),
            context,
        )

        assert response.status_code == HTTP_FOUND  # noqa: S101

    def test_create_new_product_category_empty(self) -> None:
        """Test that empty request for product category fails."""
        response = self.client.post(reverse("manager:create_new_product_category"))

        assert response.status_code == HTTP_BAD_REQUEST  # noqa: S101

    def test_create_new_product_category_invalid_empty(self) -> None:
        """Test that invalid empty request for product category fails ."""
        context = {
            "product_category_name": "",
        }

        response = self.client.post(
            reverse("manager:create_new_product_category"),
            context,
        )

        assert response.status_code == HTTP_BAD_REQUEST  # noqa: S101

    def test_create_new_product_category_invalid_too_long(self) -> None:
        """Test that invalid too long request for product category fails."""
        context = {
            "product_category_name": "asdffdsaasdffdsaasdffdsaasdffdsaasdf",
        }

        response = self.client.post(
            reverse("manager:create_new_product_category"),
            context,
        )

        assert response.status_code == HTTP_BAD_REQUEST  # noqa: S101
