from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .forms import PlayerForm
from .models import Player, Session


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


def player_list():
    pass


def player_detail(request, player_id=None, *args, **kwargs):
    player = get_object_or_404(Player, pk=player_id)
    return render(
        request,
        'overtrick/player/player.html',
        {'player': player}
    )


def player_create(request):
    print(request.user, request.user.is_authenticated)
    form = PlayerForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = PlayerForm()

    return render(request, 'overtrick/player/player.html', {'form': form})


def player_update():
    pass


def player_delete():
    pass
