from django import forms
from todo.models.task import Task
from todo.models.status_type import Status,Type


class AddTodoForm(forms.ModelForm):
    class Meta:
        model = Task
        status = forms.ModelChoiceField(
            queryset=Status.objects.all(),
            label="Статус",
            widget=forms.Select(attrs={'class': 'form-control'})
        )
        type = forms.ModelChoiceField(
            queryset=Type.objects.all(),
            label="Статус",
            widget=forms.Select(attrs={'class': 'form-control'})
        )
        fields =[
            'title',
            'description',
            'status',
            'type', ]

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }
