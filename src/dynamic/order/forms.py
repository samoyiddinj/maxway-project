from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address']
        widgets = {
            "address": forms.Textarea(attrs={
                "class": "text", "placeholder": "Enter your address", "cols": "30", "rows": "10"
            })
        }
