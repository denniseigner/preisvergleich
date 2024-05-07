from django.test import TestCase
from django.urls import reverse

from preisvergleich.models import Category

HTTP_OK = 200
HTTP_FOUND = 302
HTTP_BAD_REQUEST = 400


class PreisvergleichIndexViewTests(TestCase):
    """
    IndexView Tests.

    Methods
    -------
    test_index_view() -> None
        Test if index view returns 200

    test_index_view_shows_categories() -> None
        Test if products categories are listed on index page

    """

    def test_index_view(self) -> None:
        """Test if index view returns 200."""
        response = self.client.get(reverse("preisvergleich:index"))
        assert response.status_code == HTTP_OK  # noqa: S101

    def test_index_view_shows_categories(self) -> None:
        """Test if products categories are listed on index page."""
        category_1 = Category.objects.create(name="category_1")
        category_2 = Category.objects.create(name="category_2")

        response = self.client.get(reverse("preisvergleich:index"))
        assert response.status_code == HTTP_OK  # noqa: S101
        self.assertQuerySetEqual(
            response.context["category_list"],
            [category_1, category_2],
            ordered=False,
        )


class PreisvergleichEditorViewTests(TestCase):
    """
    IndexView Tests.

    Methods
    -------
    test_create_category_view() -> None
        Test if product category editor returns 200

    test_category_editor_delete_error_message() -> None
        Test if product category editor error message can be deleted

    test_create_new_category() -> None
        Test if new product category can be created

    test_create_new_category_empty() -> None
        Test that empty request for product category fails

    test_create_new_category_invalid_empty() -> None
        Test that invalid empty request for product category fails

    test_create_new_category_invalid_too_long() -> None
        Test that invalid too long request for product category fails

    """

    def test_create_category_view(self) -> None:
        """Test if product category editor returns 200."""
        response = self.client.get(reverse("preisvergleich:category_editor"))
        assert response.status_code == HTTP_OK  # noqa: S101

    def test_category_editor_delete_error_message(self) -> None:
        """Test if product category editor error message can be deleted."""
        response = self.client.post(reverse("preisvergleich:delete_error_message"))
        assert response.status_code == HTTP_OK  # noqa: S101
        assert response.content == b""  # noqa: S101

    def test_create_new_category(self) -> None:
        """Test if new product category can be created."""
        context = {
            "category_name": "my_name",
        }

        response = self.client.post(
            reverse("preisvergleich:create_new_category"),
            context,
        )

        assert response.status_code == HTTP_FOUND  # noqa: S101

    def test_create_new_category_empty(self) -> None:
        """Test that empty request for product category fails."""
        response = self.client.post(reverse("preisvergleich:create_new_category"))

        assert response.status_code == HTTP_BAD_REQUEST  # noqa: S101

    def test_create_new_category_invalid_empty(self) -> None:
        """Test that invalid empty request for product category fails ."""
        context = {
            "category_name": "",
        }

        response = self.client.post(
            reverse("preisvergleich:create_new_category"),
            context,
        )

        assert response.status_code == HTTP_BAD_REQUEST  # noqa: S101

    def test_create_new_category_invalid_too_long(self) -> None:
        """Test that invalid too long request for product category fails."""
        context = {
            "category_name": "asdffdsaasdffdsaasdffdsaasdffdsaasdf",
        }

        response = self.client.post(
            reverse("preisvergleich:create_new_category"),
            context,
        )

        assert response.status_code == HTTP_BAD_REQUEST  # noqa: S101
