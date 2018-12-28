from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from guestbook import models

def add(request):
    name = request.POST['name']
    password = request.POST['pass']
    content = request.POST['content']

    models.insert(( name, password, content))
    return HttpResponseRedirect('/guestbook')

def list(request):
    results = models.fetchall()
    data = {'guestbook_list' : results }
    #data는 딕셔러니로 받아온다.
    #랜더링은 html로 바꾸는 과정이다.
    return render(request, 'guestbook/list.html', data)

def delete(request):
    password= request.POST['password']
    no = request.POST['no']

    models.delete((password, no))

    return HttpResponseRedirect('/guestbook')


def deleteform(request):
    no = request.GET['no']
    data = { "no":no }
    return render(request, "guestbook/deleteform.html",data)
