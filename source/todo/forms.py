from django import forms

from todo.models import Project
from todo.models.task import Task
from todo.models.status_type import Status,Type
from django.core.exceptions import ValidationError


class AddTodoForm(forms.ModelForm):
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        label="Статус",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    type = forms.ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        label="Тип",
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )
    class Meta:
        model = Task
        fields =[
            'title',
            'description',
            'status',
            'type', ]

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        if description and title and description == title:
            raise ValidationError("Описание и название идентичны")
        return cleaned_data

class SimpleSearchForm(forms.Form):
     search = forms.CharField(max_length=100, required=False, label="")

class ProjectForm(forms.ModelForm):
   class Meta:
       model = Project
       fields =['name','description','created_at','end_at']
       widgets = {
           'name': forms.TextInput(attrs={'class':'form-control'}),
           'description': forms.Textarea(attrs={'class':'form-control'}),
           'created_at': forms.DateInput(attrs={'class':'form-control'}),
           'end_at': forms.DateInput(attrs={'class':'form-control'}),
       }
