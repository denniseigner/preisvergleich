from django.urls import path

from .views import editor_view, index_view

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
]
