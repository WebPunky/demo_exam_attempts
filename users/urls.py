from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views
# from views import hero

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(redirect_authenticated_user=True), name="login" ),
    path("logout/", LogoutView.as_view(), name="logout" ),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile")
]
