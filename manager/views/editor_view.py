from django.forms import ValidationError
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_POST, require_safe

from manager.models import ProductCategory


@require_safe
def product_category_editor(request: HttpRequest) -> HttpResponse:
    return render(request, "product_category_editor.html")


@require_safe
def delete_error_message(_: HttpRequest) -> HttpResponse:
    return HttpResponse("")


@require_POST
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
