# form
from django import forms
from .models import Inbound, Outbound, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code', 'description', 'price', 'size']
        
        
class InboundForm(forms.ModelForm):
    class Meta:
        model = Inbound
        fields = ['product', 'quantity']

class OutboundForm(forms.ModelForm):
    class Meta:
        model = Outbound
        fields = ['product', 'quantity']