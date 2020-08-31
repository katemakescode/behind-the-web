from datetime import date

from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from common.utils import LCEmailField


class Player(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    email = LCEmailField()
    phone = PhoneNumberField(blank=True, null=True)
    joined = models.DateField('date joined club', default=date.today)


class Session(models.Model):
    TIME_CHOICES = (
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
    )

    club = models.CharField(max_length=50)
    date = models.DateField(default=date.today)
    time = models.CharField(max_length=10, choices=TIME_CHOICES,
                            default='evening')
    event = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['club', 'date', 'time'],
                                    name='primary_key')
        ]
        indexes = [
            models.Index(fields=['club', '-date'])
        ]
        ordering = ('-date', 'time')

    def __str__(self):
        return f"{self.club} {self.date} {self.time}"

class Pair(models.Model):
    ORIENT_CHOICES = (
        ('ns', 'North South'),
        ('ew', 'East West'),
    )

    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    orient = models.CharField('orientation', max_length=2,
                              choices=ORIENT_CHOICES)
    pair_num = models.IntegerField()
    player_a = models.ForeignKey(Player, on_delete=models.PROTECT,
                                 related_name='sessions_as_a')
    player_b = models.ForeignKey(Player, on_delete=models.PROTECT,
                                 related_name='sessions_as_b')
    match_pts = models.IntegerField()

    class Meta:
        ordering = ('orient', '-match_pts')

    def __str__(self):
        return f"{self.orient} {self.pair_num}"

