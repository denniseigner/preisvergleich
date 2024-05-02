from django.urls import path

from . import views

app_name = "manager"
urlpatterns = [
    path("", views.index, name="index"),
    path("items/<int:item_id>/", views.detail, name="detail"),
]
