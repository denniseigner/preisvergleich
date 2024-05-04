from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_safe

from manager.models import ProductCategory


@require_safe
def index(request: HttpRequest) -> HttpResponse:
    product_categories = ProductCategory.objects.all()
    context = {
        "product_category_list": product_categories,
    }

    return render(request, "index.html", context)
