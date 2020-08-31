import datetime

from django.db import models
from django.utils import timezone

from common.utils import LCEmailField


class Subscriber(models.Model):
    email = LCEmailField(unique=True)
    created = models.DateTimeField('date subscribed', auto_now_add=True)

    def __str__(self):
        return self.email

    def was_subscribed_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=7)
