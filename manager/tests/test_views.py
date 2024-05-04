from django.test import TestCase
from django.urls import reverse

HTTP_SUCCESS = 200


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
        assert response.status_code == HTTP_SUCCESS  # noqa: S101
