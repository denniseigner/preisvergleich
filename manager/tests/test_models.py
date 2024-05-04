import pytest
from django.forms import ValidationError
from django.test import TestCase

from manager.models import Category, Product


class ManagerProductCategoryTests(TestCase):
    """
    ProductCategory Model Tests.

    Methods
    -------
    setUp() -> None
        Create a ProductCategory in DB

    test_model_str() -> None
        Test if ProductCategory String representation is correct

    """

    def setUp(self) -> None:
        """Create a ProductCategory in DB."""
        Category.objects.create(name="my_name")

    def test_model_str(self) -> None:
        """Test if ProductCategory String representation is correct."""
        test_instance = Category.objects.get(name="my_name")
        test_instance_str = str(test_instance)
        assert test_instance_str == "my_name"  # noqa: S101


class ManagerProductTests(TestCase):
    """
    Product Model Tests.

    Methods
    -------
    setUp() -> None
        Create a ProductCategory and Product in DB

    test_model_str() -> None
        Test if Product String representation is correct

    test_invalid_weight() -> None
        Test if only positive weights can be added

    test_invalid_price() -> None
        Test if only positive prices can be added

    """

    def setUp(self) -> None:
        """Create a ProductCategory and Product in DB."""
        category = Category.objects.create(name="my_name")
        Product.objects.create(
            category=category,
            name="my_name",
            shop=Product.Shops.BILLA,
            url="https://myurl.test",
            weight=100,
            price=1.5,
        )

    def test_model_str(self) -> None:
        """Test if Product String representation is correct."""
        test_instance = Product.objects.get(name="my_name")
        test_instance_str = str(test_instance)
        assert test_instance_str == "my_name 1.50€/100g"  # noqa: S101

    def test_invalid_weight(self) -> None:
        """Test if only positive weights can be added."""
        category = Category.objects.get(name="my_name")

        product = Product(
            category=category,
            name="my_name",
            shop=Product.Shops.BILLA,
            url="invalid_url",
            weight=-100,
            price=1.5,
        )
        with pytest.raises(ValidationError):
            product.full_clean()

    def test_invalid_price(self) -> None:
        """Test if only positive prices can be added."""
        category = Category.objects.get(name="my_name")

        product = Product(
            category=category,
            name="my_name",
            shop=Product.Shops.BILLA,
            url="invalid_url",
            weight=100,
            price=-1.5,
        )
        with pytest.raises(ValidationError):
            product.full_clean()
