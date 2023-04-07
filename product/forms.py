# form
from django import forms
from .models import Inbound, Outbound, Product

#제품의 틀이되는 폼
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code', 'description', 'price', 'size']
        
#제품 입고 폼    
class InboundForm(forms.ModelForm):
    class Meta:
        model = Inbound
        fields = ['product', 'quantity']
#제품 출고 폼
class OutboundForm(forms.ModelForm):
    class Meta:
        model = Outbound
        fields = ['product', 'quantity']