from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_in/', views.log_in, name='log_in'),
    path('logout/', views.logout, name='logout'),
    
]