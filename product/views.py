from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import InboundForm, ProductForm
from .models import Outbound, Product

#홈으로 사용할기능 홈으로 가기위한 함수
def home(request):
    if request.user.is_authenticated:
        return redirect('product-list')
    else:
        return redirect('/log_in') 
    

#재고 리스트 함수
@login_required
def product_list_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product/product-list.html', context)

# 재품생성하수
@login_required
def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():#폼에저장될 데이터가 폼에 입력되기 적당한지 판별하는 함수
        form.save()
        return redirect('product-list')
    context = {
        'form': form
    }
    return render(request, 'product/product.html', context)

#제품 데이터를 수정하는 함수
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

#제품 데이터 삭제 함수
@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product-list')


#제품을 입고하는 함수
@login_required
def inbound(request):
    if request.method == 'POST':
        form = InboundForm(request.POST)
        if form.is_valid():
            inbound = form.save(commit=False)
            inbound.product.stock_quantity += form.cleaned_data['quantity']
            inbound.product.save()
            inbound.save()
            return redirect('product-list')
    else:
        form = InboundForm()
    context = {
        'form': form
    }
    return render(request, 'product/inbound.html', context)



#제품을 출고하는 함수
@login_required
def outbound(request):
    if request.method == 'POST':
        form = InboundForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            stock_quantity = product.stock_quantity - quantity
            if stock_quantity < 0:
                stock_quantity = 0
            product.stock_quantity = stock_quantity
            product.save()
            Outbound.objects.create(product=product, quantity=quantity)
            return redirect('product-list')
    else:
        form = InboundForm()
    context = {
        'form': form
    }
    return render(request, 'product/outbound.html', context)

