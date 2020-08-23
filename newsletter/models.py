import datetime

from django.db import models
from django.utils import timezone


class Subscriber(models.Model):
    email_address = models.EmailField()
    created = models.DateTimeField('date subscribed', auto_now_add=True)

    def __str__(self):
        return self.email_address

    def was_subscribed_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=7)
