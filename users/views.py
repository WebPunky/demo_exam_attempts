from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from .models import User
# Create your views here.

def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:hero")
    form = RegisterForm()
    return render(request, "users/register.html", {"form": form})

@login_required
def profile(request: HttpRequest) -> HttpResponse:
    return render(request, "users/profile.html")