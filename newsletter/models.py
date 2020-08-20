from django.db import models


class Subscriber(models.Model):
    email_address = models.EmailField()
    created = models.DateTimeField('date subscribed', auto_now_add=True)
