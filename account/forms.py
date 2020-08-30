from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    error_css_class = 'error_test'
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Username', 'class': 'foo_class'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'}))

    def __init__(self, *args, **kwargs):
        self.error_messages['invalid_login'] = 'Invalid username or password'
        super().__init__(*args, **kwargs)


class RegistrationForm(LoginForm):
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={
        'placeholder': 'Email', 'autofocus': True}))

    def clean_username(self):
        pass
