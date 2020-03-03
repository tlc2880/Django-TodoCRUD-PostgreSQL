from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import TodoForm
from .models import Todo

# Name: Tommy Cao
# Original Date: 11/04/16
# Updated: 3/3/20
# Description: Django Todo Create Read Update Delete (CRUD) with PostgreSQL.
# Using 'pipenv' for virtual environment.

# Create your views here.
def todo_list(request):
    context = {'todo_list' : Todo.objects.all()}
    return render(request, 'todos/todo_list.html',context)

def todo_form(request, id=0):
    if request.method == "GET":
        if id == 0: # insert operation
            form = TodoForm()
        else:
            todo = Todo.objects.get(pk=id)
            form = TodoForm(instance=todo)
        return render(request, "todos/todo_form.html", {'form': form})
    else:
        if id == 0: # insert operation
            form = TodoForm(request.POST)
        else:
            todo = Todo.objects.get(pk=id)
            form = TodoForm(request.POST,instance= todo)
        if form.is_valid():
            form.save()
        return redirect('/todos/list')


def todo_delete(request,id):
    todo = Todo.objects.get(pk=id)
    todo.delete()
    return redirect('/todos/list/')