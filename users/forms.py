from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='Email'
    )

    role = forms.ChoiceField(
        choices=User.Role.choices,
        label='Роль'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'password1', 'password2')
