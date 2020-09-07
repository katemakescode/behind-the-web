from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import Player
from . import Session


class NSManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(orient='NS')


class EWManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(orient='EW')


class Pair(models.Model):
    ORIENT_CHOICES = (
        ('NS', _('North South')),
        ('EW', _('East West')),
    )
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    orient = models.CharField(
        'orientation',
        max_length=2,
        choices=ORIENT_CHOICES,
    )
    pair_num = models.IntegerField()
    player_a = models.ForeignKey(
        Player,
        on_delete=models.PROTECT,
        related_name='sessions_as_a',
    )
    player_b = models.ForeignKey(
        Player,
        on_delete=models.PROTECT,
        related_name='sessions_as_b',
    )
    match_pts = models.IntegerField()

    objects = models.Manager()
    ns = NSManager()
    ew = EWManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['session', 'orient', 'pair_num'],
                name='pair_pk'
            )
        ]
        ordering = ('orient', '-match_pts')

    def __str__(self):
        return f"Pair {self.pair_num} {self.orient}, {self.player_a}/" \
               f"{self.player_b}"
