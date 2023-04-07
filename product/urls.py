from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='product'),
    path('product-list/', views.product_list_view, name='product-list'),
    path('product-create/', views.create_product, name='product-create'),
    path('product-update/<int:pk>/', views.update_product, name='product-update'),
    path('product-delete/<int:pk>/', views.delete_product, name='product-delete'),
    path('inbound/', views.inbound, name='inbound'),
    path('outbound/', views.outbound, name='outbound'),
]
