from django.forms import ValidationError
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.http import require_POST, require_safe

from preisvergleich.models import Category, Product
from django.contrib import messages


@require_safe
def product_editor(request: HttpRequest, category_id: int) -> HttpResponse:
    category = get_object_or_404(Category, pk=category_id)
    context = {
        "shop_choices": Product.Shops.labels,
        "product_name": request.session.get("product_name", ""),
        "shop": request.session.get("shop", ""),
        "url": request.session.get("url", ""),
        "weight": request.session.get("weight", ""),
        "price": request.session.get("price", ""),
        "category_id": category.id,
    }
    return render(request, "product/product_editor.html", context=context)


@require_POST
def create_new_product(request: HttpRequest, category_id: int) -> HttpResponse:
    category = get_object_or_404(Category, pk=category_id)
    try:
        product_name = request.POST["product_name"]
        shop = request.POST["shop"]
        url = request.POST["url"]
        weight = request.POST["weight"]
        price = request.POST["price"]

        request.session["product_name"] = product_name
        request.session["shop"] = shop
        request.session["url"] = url
        request.session["weight"] = weight
        request.session["price"] = price
    except MultiValueDictKeyError as e:
        messages.error(request, str(e))
        return redirect("preisvergleich:product_editor", category_id=category_id)

    product = Product(
        category=category,
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
        return redirect("preisvergleich:product_editor", category_id=category_id)

    product.save()
    request.session.clear()

    return HttpResponseRedirect(reverse("preisvergleich:index"))
