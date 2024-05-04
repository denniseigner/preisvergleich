from django.urls import path

from .views import detail_view, editor_view, index_view

app_name = "manager"
urlpatterns = [
    path("", index_view.index, name="index"),
    path(
        "product_category_editor/",
        editor_view.product_category_editor,
        name="product_category_editor",
    ),
    path(
        "product_category_editor/new",
        editor_view.create_new_product_category,
        name="create_new_product_category",
    ),
    path(
        "product_category_editor/delete_error_message",
        editor_view.delete_error_message,
        name="delete_error_message",
    ),
    path(
        "product_category_detail/<int:product_category_id>",
        detail_view.product_category_detail,
        name="product_category_detail",
    ),
    path(
        "product_category_detail/<int:product_category_id>/product_editor",
        editor_view.product_editor,
        name="product_editor",
    ),
    path(
        "product_category_detail/<int:product_category_id>/product_editor/new",
        editor_view.create_new_product,
        name="create_new_product",
    ),
]
