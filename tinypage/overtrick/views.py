from django.shortcuts import render

from .models import Session


def index(request):
    return render(request, 'overtrick/index.html')


def session_list(request):
    sessions = Session.objects.all()
    return render(
        request,
        'overtrick/session/list.html',
        {'sessions_list': sessions}
    )


def session_detail(request):
    return render(request, 'overtrick/index.html')
