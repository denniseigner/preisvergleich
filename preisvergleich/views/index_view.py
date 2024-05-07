from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_safe

from preisvergleich.models import Category


@require_safe
def index(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()
    context = {
        "category_list": categories,
    }

    return render(request, "index.html", context)
