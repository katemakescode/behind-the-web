from django import forms


class RegistrationForm(forms.Form):
    email = forms.CharField()
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username'}))
    password = forms.CharField()

    def clean_username(self):
        pass
