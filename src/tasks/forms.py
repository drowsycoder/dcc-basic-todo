from django import forms
from django.forms import DateTimeInput

from .models import Task


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('completed',)
        widgets = {'due_date': DateTimeInput()}
