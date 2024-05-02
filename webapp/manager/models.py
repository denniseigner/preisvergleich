from django.db import models
from django.utils.translation import gettext_lazy as _


class Item(models.Model):
    """
    The Item model.

    Attributes
    ----------
    name : CharField
        The name of the item
    size_grams : IntegerField
        The size of the item in grams

    """

    name = models.CharField(max_length=50)
    size_grams = models.IntegerField()

    def __str__(self) -> str:
        """Return a string representation of the item."""
        return self.name


class Link(models.Model):
    """
    The Link model.

    Attributes
    ----------
    shop : CharField
        The name of the shop
    item : ForeignKey
        The link to the item
    url : URLField
        the url to the item

    """

    class Shops(models.TextChoices):
        """Shop Choices Enum."""

        BILLA = "Billa", _("Billa")
        HOFER = "Hofer", _("Hofer")

    shop = models.CharField(max_length=50, choices=Shops.choices, default=Shops.HOFER)
    item = models.ForeignKey(
        "Item",
        on_delete=models.DO_NOTHING,
    )
    url = models.URLField()

    def __str__(self) -> str:
        """Return a string representation of the link."""
        return self.shop
