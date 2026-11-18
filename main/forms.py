from django import forms
from django.forms import widgets
from django.utils import timezone
from django.core.exceptions import ValidationError

from .models import Orders

class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ("services", "scheduledd_at",)
        widgets = {
            "scheduledd_at": forms.DateTimeInput(attrs={"type": "date"})
        }
    def clean_scheduledd_at(self):
        value = self.cleaned_data["scheduledd_at"]
        if value < timezone.now():
            raise forms.ValidationError("Нельзя выбрать прошедшую дату")
        return value