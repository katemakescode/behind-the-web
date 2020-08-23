from django.shortcuts import render
from django.http import HttpResponse

from .models import Subscriber


def subscriber_list():
    pass


def subscriber_get(request, *args, **kwargs):
    obj = Subscriber.objects.get(id=1)
    return HttpResponse(f'<h1>Hello {obj}</h1>')


def subscriber_create():
    pass


def subscriber_update():
    pass


def subscriber_delete():
    pass
