from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductCategory(models.Model):
    """
    The ProductCategory model.

    Attributes
    ----------
    name : CharField
        The name of the ProductCategory

    """

    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        """Return a string representation of the ProductCategory."""
        return self.name


class Product(models.Model):
    """
    The Product model.

    Attributes
    ----------
    product_category : ForeignKey
        The associated ProductCategory
    name : CharField
        The name of the product
    shop : CharField
        The shop the product can be found
    url : URLField
        The url to the product
    weight : IntegerField
        The weight of the product
    price : DecimalField
        The price of the product

    """

    class Shops(models.TextChoices):
        """Shop Choices Enum."""

        BILLA = "Billa", _("Billa")
        HOFER = "Hofer", _("Hofer")

    product_category = models.ForeignKey(
        "ProductCategory",
        on_delete=models.DO_NOTHING,
    )
    name = models.CharField(max_length=32)
    shop = models.CharField(max_length=32, choices=Shops.choices, default=Shops.HOFER)
    url = models.URLField()
    weight = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    def __str__(self) -> str:
        """Return a string representation of the product."""
        return f"{self.name} {self.price}€/{self.weight}g"
