

# Create your views here.
#view 
"""
장고에서 제공하는 기능을 최대한 사용해 구현해봅시다.
아래 from ... import ... 구문이 힌트입니다. 
지금은 해당 함수가 어떻게 구현되어있는지 전부다 이해 할 수는 없겠지만 
지금까지 공부한 내용으로 이해할 수 있는 부분이 있을겁니다.
모르는 부분이 있다면 지금입니다. 공부할 타이밍!
"""
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse


def sign_up(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('log_in')
    else:
        form = UserForm()
    return render(request, 'users/sign_up.html', {'form': form})
    
    
def log_in(request): # 함수 이름을 변경
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
    return render(request, 'users/log_in.html', {'form': form})

# @login_required        
# def user_logout(request):
#     auth.logout(request)
#     return redirect('/')



