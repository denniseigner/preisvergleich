from django.forms import ValidationError
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.http import require_POST, require_safe
from django.contrib import messages
from django.shortcuts import render, redirect
from preisvergleich.models import Category


@require_safe
def category_editor(request: HttpRequest) -> HttpResponse:
    context = {
        "category_name": request.session.get("category_name", ""),
    }
    return render(request, "category/category_editor.html", context)


@require_POST
def create_new_category(request: HttpRequest) -> HttpResponse:
    try:
        category_name = request.POST["category_name"]
        request.session["category_name"] = category_name
    except MultiValueDictKeyError as e:
        messages.error(str(e))
        return redirect("preisvergleich:category_editor")

    category = Category(
        name=category_name,
    )

    try:
        category.full_clean()
    except ValidationError as e:
        messages.error(str(e))
        return redirect("preisvergleich:category_editor")

    category.save()
    request.session.clear()

    return HttpResponseRedirect(reverse("preisvergleich:index"))
