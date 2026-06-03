from django import forms
from todo.models import Task


class AddTodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','status','end_date']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'end_date': forms.DateInput(attrs={'class':'form-control'}),
        }