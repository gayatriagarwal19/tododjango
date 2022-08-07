from ast import Mod
from dataclasses import field, fields
from pyexpat import model
from django.forms import ModelForm
from todo.models import todo

class todoForm(ModelForm):
    class Meta:
        model = todo
        fields = ['title', 'description', 'status']