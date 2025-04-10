from django.shortcuts import render, redirect
from home.models import *
from django.contrib import messages


def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', context={'todos': todos})

def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'details.html', context={'todo':todo})

def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'todo deleted successfully', 'success')
    return redirect('home')