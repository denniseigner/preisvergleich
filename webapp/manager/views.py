from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Item


def index(request: HttpRequest) -> HttpResponse:
    item_list = Item.objects.all()
    context = {"item_list": item_list}
    return render(request, "index.html", context)


def detail(request: HttpRequest, item_id: int) -> HttpResponse:
    item = get_object_or_404(Item, pk=item_id)
    return render(request, "detail.html", {"item": item})


def editor(request: HttpRequest) -> HttpResponse:
    return render(request, "editor.html")


def create_new(request: HttpRequest) -> HttpResponse:
    try:
        created_item = Item.objects.create(
            name=request.POST["item_name"],
            size_grams=request.POST["size_grams"],
        )
    except ValueError as e:
        return render(request, "editor.html", {"error_message": e})
    return HttpResponseRedirect(reverse("manager:detail", args=(created_item.id,)))
