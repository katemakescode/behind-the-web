from django.contrib import admin

from .models import Session, Pair, Player

admin.site.register(Pair)
admin.site.register(Player)
admin.site.register(Session)
