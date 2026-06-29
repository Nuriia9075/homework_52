from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email", )
    last_name = forms.CharField(label="Фамилия", required=False)
    first_name = forms.CharField(label="Имя", required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean(self):
        cleaned_data = super().clean()
        last_name = cleaned_data.get('last_name')
        firstname = cleaned_data.get('first_name')
        if last_name or firstname:
            return cleaned_data
        raise ValidationError("Заполните хотя бы одно из полей: Имя или Фамилия")