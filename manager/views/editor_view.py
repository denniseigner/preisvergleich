from django.forms import ValidationError
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.http import require_POST, require_safe

from manager.models import ProductCategory

PRODUCT_CATEGORY_EDITOR_HTML = "product_category_editor.html"


@require_safe
def product_category_editor(request: HttpRequest) -> HttpResponse:
    return render(request, PRODUCT_CATEGORY_EDITOR_HTML)


@require_safe
def delete_error_message(_: HttpRequest) -> HttpResponse:
    return HttpResponse("")


@require_POST
def create_new_product_category(request: HttpRequest) -> HttpResponse:
    try:
        product_category_name = request.POST["product_category_name"]
    except MultiValueDictKeyError as e:
        context = {
            "error_message": str(e),
        }
        return render(request, PRODUCT_CATEGORY_EDITOR_HTML, context, status=400)

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
        return render(request, PRODUCT_CATEGORY_EDITOR_HTML, context, status=400)

    product_category.save()

    return HttpResponseRedirect(reverse("manager:index"))
