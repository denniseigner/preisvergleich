from django.urls import path

from .views import category_detail_view, category_editor_view, helper_views, index_view

app_name = "manager"
urlpatterns = [
    path("", index_view.index, name="index"),
    path(
        "category_editor/",
        category_editor_view.category_editor,
        name="category_editor",
    ),
    path(
        "category_editor/new",
        category_editor_view.create_new_category,
        name="create_new_category",
    ),
    path(
        "category_editor/delete_error_message",
        helper_views.delete_error_message,
        name="delete_error_message",
    ),
    path(
        "category_detail/<int:category_id>",
        category_detail_view.category_detail,
        name="category_detail",
    ),
]
