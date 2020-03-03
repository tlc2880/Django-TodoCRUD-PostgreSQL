# Name: Tommy Cao
# Original Date: 11/04/16
# Updated: 3/3/20
# Description: Django Todo Create Read Update Delete (CRUD) with PostgreSQL.
# Using 'pipenv' for virtual environment.

from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('content','priority')
        labels = {
            'content':'Task',
            'priority':'Priority'
        }

    def __init__(self, *args, **kwargs):
        super(TodoForm,self).__init__(*args, **kwargs)
        self.fields['priority'].empty_label = "Select"
