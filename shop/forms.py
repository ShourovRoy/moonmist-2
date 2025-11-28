from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=20, initial=1)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
