from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from manager.models import ProductCategory


def index(request: HttpRequest) -> HttpResponse:
    product_categories = ProductCategory.objects.all()
    context = {
        "product_category_list": product_categories,
    }

    return render(request, "index.html", context)
