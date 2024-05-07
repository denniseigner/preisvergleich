from django.urls import path

from .views import (
    category_detail_view,
    category_editor_view,
    helper_views,
    index_view,
    product_editor_view,
)

app_name = "preisvergleich"

# fmt: off
urlpatterns = [
    # Index view
    path("", index_view.index, name="index"),

    # Helper views
    path("delete_error_message", helper_views.delete_error_message, name="delete_error_message"),

    # Category editor views
    path("category_editor/", category_editor_view.category_editor, name="category_editor"),
    path("category_editor/new", category_editor_view.create_new_category, name="create_new_category"),

    # Category detail view
    path("category_detail/<int:category_id>", category_detail_view.category_detail, name="category_detail"),

    # Product editor views
    path("product_editor/<int:category_id>", product_editor_view.product_editor, name="product_editor"),
    path("product_editor/<int:category_id>/new", product_editor_view.create_new_product, name="create_new_product"),
]
# fmt: on
