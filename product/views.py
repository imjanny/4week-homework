from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import ProductForm
from .models import Product

def home(request):
    if request.user.is_authenticated:
        return redirect('product-list')
    else:
        return redirect('/log_in')

@login_required
def product_list_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product/product-list.html', context)

@login_required
def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product-list')
    context = {
        'form': form
    }
    return render(request, 'product/product.html', context)

@login_required
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product-list')
    context = {
        'form': form,
        'product': product
    }
    return render(request, 'product/product.html', context)

@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product-list')
