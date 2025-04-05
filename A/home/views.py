from django.shortcuts import render
from home.models import *


def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', context={'todos': todos})

def hello(request):
    return render(request, 'hello.html', context={'name':'mobin'})