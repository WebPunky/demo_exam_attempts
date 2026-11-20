from django.urls import path

from . import views

# from views import hero

app_name = "main"

urlpatterns = [
    path("hero/", views.hero, name="hero"),
    path("create_order/", views.create_order, name="create_order"),
    path("list_order/", views.list_order, name="list_order"),
    path("<int:order_id>/create_review/", views.create_review, name="create_review"),
]
