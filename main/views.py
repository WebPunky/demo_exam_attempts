from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .models import Services, Orders, Reviews
from .forms import CreateOrderForm, ReviewForm

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
    orders = Orders.objects.filter(user=request.user)
    return render(request, "main/list_order.html", {"orders": orders})

@login_required
def create_review(request: HttpRequest, order_id: int) -> HttpResponse:
    order = get_object_or_404(Orders, id=order_id, user=request.user)

    if order.status != Orders.Status.DONE:
        raise PermissionDenied

    if Reviews.objects.filter(order=order).exists():
        return redirect("main:list_order")

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.order = order
            review.save()
            return redirect("main:list_order")
    else:
        form = ReviewForm()

        return render(request, "main/create_review.html", {"form": form})
