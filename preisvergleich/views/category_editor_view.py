from django.contrib import messages
from django.forms import ValidationError
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_POST, require_safe

from preisvergleich.models import Category


@require_safe
def category_editor(request: HttpRequest) -> HttpResponse:
    context = {
        "category_name": request.session.get("category_name", ""),
    }
    return render(request, "category/category_editor.html", context)


@require_POST
def create_new_category(request: HttpRequest) -> HttpResponse:

    category_name = request.POST.get("category_name", "")
    request.session["category_name"] = category_name

    if not category_name:
        messages.error(request, "Category name is required.")
        context = {"category_name": category_name}
        return render(request, "category/category_editor.html", context=context)

    category = Category(
        name=category_name,
    )

    try:
        category.full_clean()
    except ValidationError as e:
        messages.error(request, e.messages)
        context = {"category_name": category_name}
        return render(request, "category/category_editor.html", context=context)

    category.save()
    request.session.clear()
    return HttpResponseRedirect(reverse("preisvergleich:index"))
