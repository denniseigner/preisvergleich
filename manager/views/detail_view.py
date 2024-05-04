from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from manager.models import ProductCategory


def product_category_detail(
    request: HttpRequest,
    product_category_id: int,
) -> HttpResponse:
    product_category = get_object_or_404(ProductCategory, pk=product_category_id)

    context = {"product_category": product_category}

    return render(request, "product_category_detail.html", context)
