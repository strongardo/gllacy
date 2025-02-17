from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Введите действующий адрес электронной почты.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        help_texts = {
            'username': 'Не более 150 символов.',
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

        help_texts = {
            'username': 'Не более 150 символов.',
        }
