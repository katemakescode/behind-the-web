from django.db import models


class Subscriber(models.Model):
    email_address = models.EmailField()
