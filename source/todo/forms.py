from django import forms
from todo.models.task import Task


class AddTodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','status','type']
