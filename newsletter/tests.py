from django.test import TestCase

from .models import Subscriber


class SubscriberModelTests(TestCase):

    def test_subscriber_email_address(self):
        subscriber = Subscriber(email_address='test@test.com')
        self.assertIs(subscriber.email_address, 'test@test.com')
