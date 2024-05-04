from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from manager.models import Category


def category_detail(
    request: HttpRequest,
    category_id: int,
) -> HttpResponse:
    category = get_object_or_404(Category, pk=category_id)

    context = {"category": category}

    return render(request, "category/category_detail.html", context)
