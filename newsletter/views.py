from django.shortcuts import render
from django.http import Http404

from .forms import SubscriberForm
from .models import Subscriber


def subscriber_list():
    pass


def subscriber_get(request, id_=None, *args, **kwargs):
    try:
        subscriber = Subscriber.objects.get(id=id_)
    except Subscriber.DoesNotExist:
        raise Http404

    return render(request, 'newsletter/subscriber.html', {'subscriber':
                                                          subscriber})


def subscriber_create(request):
    form = SubscriberForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = SubscriberForm()

    return render(request, 'newsletter/subscribe.html', {'form': form})


def subscriber_update():
    pass


def subscriber_delete():
    pass
