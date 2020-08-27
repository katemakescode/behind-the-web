import datetime

from django.db import models
from django.utils import timezone


class LCEmailField(models.EmailField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()


class Subscriber(models.Model):
    email = LCEmailField(unique=True)
    created = models.DateTimeField('date subscribed', auto_now_add=True)

    def __str__(self):
        return self.email

    def was_subscribed_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=7)
