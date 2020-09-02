from django.http import Http404
from django.shortcuts import render

from .forms import SubscriberForm
from .models import Subscriber


def subscriber_list():
    pass


def subscriber_get(request, subscriber_id=None, *args, **kwargs):
    try:
        subscriber = Subscriber.objects.get(id=subscriber_id)
    except Subscriber.DoesNotExist:
        raise Http404

    return render(request, 'newsletter/subscriber.html', {'subscriber':
                                                              subscriber})


def subscriber_create(request):
    print(request.user, request.user.is_authenticated)
    form = SubscriberForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = SubscriberForm()

    return render(request, 'newsletter/subscribe.html', {'form': form})


def subscriber_update():
    pass


def subscriber_delete():
    pass
