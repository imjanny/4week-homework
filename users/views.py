from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .forms import UserForm, LoginForm
from django.http import HttpResponse

# 회원가입 기능 구현 함수
def sign_up(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return render(request, 'users/log_in.html', {'form': form})
    else:
        form = UserForm()
    return render(request, 'users/sign_up.html', {'form': form})
    
# 로그인 기능 구현 함수
def log_in(request): # 함수 이름을 변경
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
    return render(request, 'users/log_in.html', {'form': form})
#로그아웃 기능 구현 함수
@login_required        
def logout(request):
    auth.logout(request)
    return redirect('/')


