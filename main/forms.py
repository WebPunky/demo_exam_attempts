from django import forms

from .models import Orders

class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ("scheduledd_at", "services",)