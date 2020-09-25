from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm


def send_user_message(form):
    return send_mail(
        subject=f"TinyPager: "
                f"{form.cleaned_data['name']}"
                f"({form.cleaned_data['email']})",
        message=form.cleaned_data['message'],
        from_email=form.cleaned_data['email'],
        recipient_list=[settings.DEFAULT_TO_EMAIL],
        fail_silently=False,
    )


def send_autoreply(form):
    return send_mail(
        subject='Hello from Behind the Web',
        message="Hi!\n\nIf you're seeing this, it's most likely because you "
                "sent me a message from my website. This here is just an "
                "automatic reply, but I'll get back to you for real as soon "
                "as I can.\n\nKate",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[form.cleaned_data['email']],
        fail_silently=False,
    )


def build_message_context(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sent = send_user_message(form)
            send_autoreply(form)
        else:
            form = ContactForm()
        context = dict(form=form, sent=sent)
        return context


def message_send(request):
    context = build_message_context(request)
    return render(request, 'contact/message.html', context)
