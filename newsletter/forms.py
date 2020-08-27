from django import forms

from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email_address']

    def clean_email_address(self):
        email_address = self.cleaned_data.get("email_address")
        qs = Subscriber.objects.filter(email_address__iexact=email_address)
        if qs.exists():
            raise forms.ValidationError("You have already subscribed")
        return email_address
