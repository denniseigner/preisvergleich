from django.forms import ValidationError
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from manager.models import ProductCategory


def product_category_editor(request: HttpRequest) -> HttpResponse:
    return render(request, "product_category_editor.html")


def delete_error_message(_: HttpRequest) -> HttpResponse:
    return HttpResponse("")


def create_new_product_category(request: HttpRequest) -> HttpResponse:
    product_category_name = request.POST["product_category_name"]

    product_category = ProductCategory(
        name=product_category_name,
    )

    try:
        product_category.full_clean()
    except ValidationError as e:
        context = {
            "error_message": str(e),
            "product_category_name": product_category_name,
        }
        return render(request, "product_category_editor.html", context)

    product_category.save()

    return HttpResponseRedirect(reverse("manager:index"))
