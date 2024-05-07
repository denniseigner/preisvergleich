from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    """
    The Category model.

    Attributes
    ----------
    name : CharField
        The name of the Category

    """

    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        """Return a string representation of the Category."""
        return self.name


class Product(models.Model):
    """
    The Product model.

    Attributes
    ----------
    category : ForeignKey
        The associated Category
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

        BILLA = "Billa"
        HOFER = "Hofer"

    category = models.ForeignKey(
        "Category",
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
