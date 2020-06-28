from django.test import TestCase
from django.db.utils import IntegrityError
from .models.formMessage import FormMessage

class TestModels(TestCase):
    def test_no_empty_customer(self):
        ''' Make sure there can't be a message without customer '''

        message = FormMessage(
            additional_message = 'test message'
        )
        with self.assertRaises(IntegrityError, msg='message without customer should not be allowed'):
            message.save()