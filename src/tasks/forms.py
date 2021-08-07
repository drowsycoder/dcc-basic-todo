from django import forms
from django.forms import DateTimeInput

from .models import Task


class TaskModelForm(forms.ModelForm):
    """Form class for Task model."""

    class Meta:
        model = Task
        exclude = ('completed',)
        widgets = {'due_date': DateTimeInput()}
