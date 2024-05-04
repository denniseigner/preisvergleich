from django.forms import ValidationError
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.http import require_POST, require_safe

from manager.models import Category

CATEGORY_EDITOR_HTML = "category/category_editor.html"


@require_safe
def category_editor(request: HttpRequest) -> HttpResponse:
    return render(request, CATEGORY_EDITOR_HTML)


@require_POST
def create_new_category(request: HttpRequest) -> HttpResponse:
    try:
        category_name = request.POST["category_name"]
    except MultiValueDictKeyError as e:
        context = {
            "error_message": str(e),
        }
        return render(request, CATEGORY_EDITOR_HTML, context, status=400)

    category = Category(
        name=category_name,
    )

    try:
        category.full_clean()
    except ValidationError as e:
        context = {
            "error_message": str(e),
            "category_name": category_name,
        }
        return render(request, CATEGORY_EDITOR_HTML, context, status=400)

    category.save()

    return HttpResponseRedirect(reverse("manager:index"))
