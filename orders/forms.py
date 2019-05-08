from django import forms
from orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class FilterForm(forms.Form):
    FIELDS_CHOICE = {
        ('marketplace','Marketplace'),
        ('amount', 'Amount'),
        ('shipping', 'Shipping'),
        ('address', 'Address'),
        ('last_name', 'Lastname'),
        ('city', 'City'),
        ('all', '')
    }

    field = forms.ChoiceField(choices=FIELDS_CHOICE, required=True)
    search = forms.CharField(max_length=50, required=False)