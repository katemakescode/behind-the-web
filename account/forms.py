from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'}))


class RegistrationForm(LoginForm):
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={
        'placeholder': 'Email', 'autofocus': True}))

    def clean_username(self):
        pass
