from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Item


def index(request: HttpRequest) -> HttpResponse:
    item_list = Item.objects.all()
    context = {"item_list": item_list}
    return render(request, "index.html", context)


def detail(request: HttpRequest, item_id: int) -> HttpResponse:
    item = get_object_or_404(Item, pk=item_id)
    return render(request, "detail.html", {"item": item})
