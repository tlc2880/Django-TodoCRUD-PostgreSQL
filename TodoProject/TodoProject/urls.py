"""TodoProject URL Configuration

# Name: Tommy Cao
# Original Date: 11/04/16
# Updated: 3/3/20
# Description: Django Todo Create Read Update Delete (CRUD) with PostgreSQL.
# Using 'pipenv' for virtual environment.

"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/',include('todos.urls'))
]
