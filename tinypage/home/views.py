from django.conf import settings
from django.shortcuts import render

from contact.views import build_message_context


def index(request):
    context = build_message_context(request)
    context['overtrick_url'] = settings.OVERTRICK_URL
    return render(request, 'home/index.html', context)
