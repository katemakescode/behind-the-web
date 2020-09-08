from django.shortcuts import render

from .forms import ContactForm


def message_send(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ContactForm()
    return render(request, 'contact/message.html', {'form': form})
