from django.shortcuts import render
from home.models import *


def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', context={'todos': todos})

def hello(request):
    return render(request, 'hello.html', context={'name':'mobin'})

def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'details.html', context={'todo':todo})