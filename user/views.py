from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from user import models


# Create your views here.

def joinform(request):
    return render(request, 'user/joinform.html')

def join(request):
    name  = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    gender = request.POST['gender']

    data_tuple = (name, email, password, gender)
    models.insert(data_tuple)
    return HttpResponseRedirect('/user/joinsuccess')

def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')

def loginform(requset):
    return render(requset, 'user/loginform.html')

def login(request):
    email = request.POST['email']
    password = request.POST['password']

    user = models.get(email, password)

    #로그인 실패
    if user is None:
        return HttpResponseRedirect('/user/loginform?result=fail')

    #로그인 성공(처리)

    # 브라우저가 장고에게 요청을 보낼때 쿠키가 없으면 쿠키를 만들어서 브라우저에게 주고 브라우저가 쿠키를 디스크혹은 메모리에 저장
    # 쿠키가 있으면 서버에게 요청 넘기고  Session에서 쿠키정보를 찾아서 보내준다.
    # 서버가 request을 보고 session이름에 맞는(['authuser']) 쿠키를 찾아서 보낸다.
    # session은 쿠키이름이 같은 걸 모아둔것
    request.session['authuser']= user
    #main으로 리다이렉트
    return HttpResponseRedirect('/')

def logout(request):
    del request.session['authuser']
    return  HttpResponseRedirect('/')