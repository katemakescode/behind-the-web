from datetime import date

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Session(models.Model):
    TIME_CHOICES = (
        ('morning', _('Morning')),
        ('afternoon', _('Afternoon')),
        ('evening', _('Evening')),
    )

    club = models.CharField(max_length=50)
    date = models.DateField(default=date.today)
    time = models.CharField(
        max_length=10,
        choices=TIME_CHOICES,
        default='evening',
    )
    event = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)

    @property
    def full_club(self):
        return f'{self.club} Bridge Club'

    @property
    def full_time(self):
        weekday_name = self.date.strftime('%A')
        return f'{weekday_name} {self.time}'

    @property
    def winning_pairs(self):
        return {
            'NS': self.pair_set(manager='ns').first(),
            'EW': self.pair_set(manager='ew').first()
        }

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['club', 'date', 'time'],
                name='session_pk',
            )
        ]
        indexes = [
            models.Index(fields=['club', '-date'])
        ]
        ordering = ('-date', 'time')

    def __str__(self):
        return f"{self.club} {self.date} {self.time}"

    def get_absolute_url(self):
        return reverse(
            'overtrick:sessions-detail',
            args=[self.club.lower(),
                  self.date.year, self.date.month, self.date.day,
                  self.time]
        )
