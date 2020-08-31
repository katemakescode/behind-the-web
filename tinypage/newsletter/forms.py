from django import forms

from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = Subscriber.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("You have already subscribed")
        return email
