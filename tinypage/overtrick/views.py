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


# def session_detail(request, club, year, month, day, time):
def session_detail(request, session_id):
    #     session = get_object_or_404(
    #         Session,
    #         club=club,
    #         date__year=year,
    #         date__month=month,
    #         date__day=day,
    #         time=time,

    session = get_object_or_404(
        Session,
        pk=session_id,
    )

    return render(
        request,
        'overtrick/session/detail.html',
        {'session': session}
    )
