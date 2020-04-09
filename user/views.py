from re import match

from django.shortcuts import render, redirect
from user import models


def home(request):
    login_name = ''
    if request.session.get('id'):
        user = models.User.objects.get(id=request.session.get('id'))
        login_name = user.username
    return render(request, 'index.html', {"name": login_name})


def login(request):
    if request.session.get('id') is not None:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            username = username.strip()  # 去除空格和换行
            password = password.strip()
            try:
                user = models.User.objects.get(username=username)
            except:
                message = '该用户名不存在'
                return render(request, 'login.html', {"message": message})
            if user.password == password:
                request.session['id'] = user.id  # 记录用户已登录
                return redirect('/')
            else:
                message = '密码错误'
                return render(request, 'login.html', {"message": message})
    return render(request, 'login.html')


def register(request):
    if request.session.get('id') is not None:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        username = username.strip()
        password = password.strip()
        if models.User.objects.filter(username=username).exists():
            message = '该用户名已被注册'
            return render(request, 'register.html', {"message": message})
        if not match('[BHQ]\d{8}', username):
            message = '该用户名不合法'
            return render(request, 'register.html', {"message": message})
        user = models.User()
        user.username = username
        user.password = password
        user.save()
        request.session['id'] = user.id  # 记录用户已登录
        return redirect('/')
    return render(request, 'register.html')


def logout(request):
    request.session.flush()
    return redirect('/')


def setting(request):
    if request.session.get('id') is None:
        message = '请登录'
        return render(request, 'login.html', {"message": message})
    user = models.User.objects.get(id=request.session.get('id'))
    login_name = user.username
    return render(request, 'settings.html', {"name": login_name})
