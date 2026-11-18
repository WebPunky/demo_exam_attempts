from django.urls import path

from . import views

# from views import hero

APP_NAME = "main"

urlpatterns = [
    path("hero/", views.hero, name="hero"),
    path("create_order/", views.create_order, name="create_order"),
    path("list_order/", views.list_order, name="list_order"),
]
