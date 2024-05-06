from django.forms import ValidationError
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.http import require_POST, require_safe

from manager.models import Category, Product
from django.contrib import messages


@require_safe
def product_editor(request: HttpRequest) -> HttpResponse:
    context = {"shop_choices": Product.Shops.labels}
    return render(request, "product/product_editor.html", context=context)


@require_POST
def create_new_product(request: HttpRequest) -> HttpResponse:
    try:
        product_name = request.POST["product_name"]
        shop = request.POST["shop"]
        url = request.POST["url"]
        weight = request.POST["weight"]
        price = request.POST["price"]
    except MultiValueDictKeyError as e:
        messages.error(request, str(e))
        return redirect("manager:product_editor")

    product = Product(
        name=product_name,
        shop=shop,
        url=url,
        weight=weight,
        price=price,
    )

    try:
        product.full_clean()
    except ValidationError as e:
        messages.error(request, str(e))
        return redirect("manager:product_editor")

    product.save()

    return HttpResponseRedirect(reverse("manager:index"))
