from django.shortcuts import render, redirect
from home.models import *
from django.contrib import messages
from .forms import TodoCreateForm


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

def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], body=cd['body'], created_at=cd['created_at'])
            messages.success(request, 'Todo created successfully', 'success')
            return redirect('home')
    else:
        form = TodoCreateForm()
    return render(request, 'create.html', context={'form': form})