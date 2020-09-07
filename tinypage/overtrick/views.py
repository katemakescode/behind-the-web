from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Session


def index(request):
    return render(request, 'overtrick/index.html')


class SessionListView(ListView):
    model = Session
    template_name = 'overtrick/session/list.html'


def session_detail(request, club, year, month, day, time):
    session = get_object_or_404(
        Session,
        club__iexact=club,
        date__year=year,
        date__month=month,
        date__day=day,
        time=time
    )

    pairs = session.pair_set.all()

    return render(
        request,
        'overtrick/session/detail.html',
        {
            'session': session,
            'pairs_list': pairs,
        }
    )
