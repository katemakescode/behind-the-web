from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Subscriber


def subscriber_list():
    pass


def subscriber_get(request, id_=None, *args, **kwargs):
    try:
        obj = Subscriber.objects.get(id=id_)
    except Subscriber.DoesNotExist:
        raise Http404

    return HttpResponse(f'<h1>Hello {obj}</h1>')


def subscriber_create():
    pass


def subscriber_update():
    pass


def subscriber_delete():
    pass
