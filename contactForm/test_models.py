from django.test import TestCase
from django.db.utils import IntegrityError
from .models.contactMessage import ContactMessage

class TestModels(TestCase):
    def test_no_empty_customer(self):
        ''' Make sure there can't be a message without customer '''

        message = ContactMessage(
            subject = 'test subject',
            message = 'test message'
        )
        with self.assertRaises(IntegrityError):
            message.save()