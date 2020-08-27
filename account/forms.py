from django import forms


class RegistrationForm(forms.Form):
    email = forms.CharField()
    username = forms.CharField()
    password = forms.CharField()
