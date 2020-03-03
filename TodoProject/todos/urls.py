# Name: Tommy Cao
# Original Date: 11/04/16
# Updated: 3/3/20
# Description: Django Todo Create Read Update Delete (CRUD) with PostgreSQL.
# Using 'pipenv' for virtual environment.

from django.urls import path
from . import views

urlpatterns =[
    path('', views.todo_form,name='todo_insert'), # get and post request for insert operation
    path('<int:id>/', views.todo_form,name='todo_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.todo_delete,name='todo_delete'),
    path('list/',views.todo_list,name='todo_list') # get request to retrieve and display all records
]