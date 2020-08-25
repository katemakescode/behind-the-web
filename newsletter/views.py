from django.shortcuts import render
from django.http import Http404

from .models import Subscriber


def subscriber_list():
    pass


def subscriber_get(request, id_=None, *args, **kwargs):
    try:
        subscriber = Subscriber.objects.get(id=id_)
    except Subscriber.DoesNotExist:
        raise Http404

    return render(request, 'get.html', {'subscriber': subscriber})


def subscriber_create():
    pass


def subscriber_update():
    pass


def subscriber_delete():
    pass
