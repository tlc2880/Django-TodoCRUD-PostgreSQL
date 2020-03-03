# Name: Tommy Cao
# Original Date: 11/04/16
# Updated: 3/3/20
# Description: Django Todo Create Read Update Delete (CRUD) with PostgreSQL.
# Using 'pipenv' for virtual environment.

from django.db import models

# Create your models here.
class Priority(models.Model):
    priority = models.CharField(max_length=50)

    def __str__(self):
        return self.priority

class Todo(models.Model):
    content = models.TextField(max_length=100)
    priority= models.ForeignKey(Priority,on_delete=models.CASCADE)