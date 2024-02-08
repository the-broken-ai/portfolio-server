from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("models", views.my_model_view, name="my_model_view")
]