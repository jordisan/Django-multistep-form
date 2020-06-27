from django.test import TestCase
from django.db.utils import IntegrityError
from .models.formMessage import FormMessage

class TestModels(TestCase):
    def test_no_empty_customer(self):
        ''' Make sure there can't be a message without customer '''

        message = FormMessage(
            subject = 'test subject',
            message = 'test message'
        )
        with self.assertRaises(IntegrityError):
            message.save()