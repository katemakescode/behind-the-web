from django.contrib import admin

from .models import Pair, Player, Session


@admin.register(Pair)
class PairAdmin(admin.ModelAdmin):
    pass


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_filter = ('joined',)
    search_fields = ('first_name', 'last_name')


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('club', 'date', 'time', 'event')
    list_filter = ('club', 'date')
    search_fields = ('event',)
