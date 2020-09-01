from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': _('Username')}),
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': _('Password')}),
    )

    def __init__(self, *args, **kwargs):
        self.error_messages['invalid_login'] = _(
            'Invalid username or password'
        )
        super().__init__(*args, **kwargs)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': _('Password')})
    )

    class Meta:
        model = User
        fields = ('email', 'username')
        help_texts = {
            'username': ''
        }
        labels = {
            'email': '',
            'username': '',
        }
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': _('Email')}),
            'username': forms.TextInput(attrs={'placeholder': _('Username')}),
        }

    def clean(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError(_('An email address is required'))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise ValidationError(
                _(f'The email {email} is already registered')
            )
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise ValidationError(
                _(f'The username {username} is already registered')
            )
        return username
