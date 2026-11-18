from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Services, Orders
from .forms import CreateOrderForm

def hero(request: HttpRequest) -> HttpResponse:
    services = Services.objects.all()
    return render(request, "main/hero.html", {"services": services})

@login_required
def create_order(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CreateOrderForm(request.POST)
        print(form.errors)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect("main:hero")
    form = CreateOrderForm()
    return render(request, "main/create_order.html", {"form": form})

@login_required
def list_order(request: HttpRequest) -> HttpResponse:
    orders = Orders.objects.all()
    return render(request, "main/list_order.html", {"orders": orders})