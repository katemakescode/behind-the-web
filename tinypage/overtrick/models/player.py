from datetime import date

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from common.utils import LCEmailField


class Player(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    email = LCEmailField()
    phone = PhoneNumberField(blank=True, null=True)
    joined = models.DateField(_('date player joined club'), default=date.today)

    class Meta:
        indexes = [
            models.Index(fields=['last_name', 'first_name'])
        ]
        ordering = ('last_name', 'first_name')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        qs = Player.objects.filter(
            first_name__iexact=self.first_name,
            last_name__iexact=self.last_name
        )
        if qs.exists():
            raise ValidationError(
                _('Player names must be unique regardless of case.')
            )
