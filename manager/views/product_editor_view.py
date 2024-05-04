from django.forms import ValidationError
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.http import require_POST, require_safe

from manager.models import Category


@require_safe
def product_editor(request: HttpRequest) -> HttpResponse:
    return render(request, "product/product_editor.html")
