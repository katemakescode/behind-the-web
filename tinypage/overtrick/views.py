from django.shortcuts import get_object_or_404, render

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
