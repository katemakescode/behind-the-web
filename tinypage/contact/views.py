from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm


#
def message_send(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            result = send_mail(
                subject=f"TinyPage message received from "
                        f"{form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=[settings.DEFAULT_TO_EMAIL],
                fail_silently=False,
            )
    else:
        form = ContactForm()
    return render(request, 'contact/message.html', {'form': form})
