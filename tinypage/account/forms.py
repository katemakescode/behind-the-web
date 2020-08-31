from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'}))

    def __init__(self, *args, **kwargs):
        self.error_messages['invalid_login'] = 'Invalid username or password'
        super().__init__(*args, **kwargs)


class RegistrationForm(LoginForm):
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={
        'placeholder': 'Email', 'autofocus': True}))

    field_order = ['email', 'username', 'password']

    def clean_username(self):
        pass
