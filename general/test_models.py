from django.test import TestCase
from general.models.customer import Customer
from django.db.utils import IntegrityError

class TestModels(TestCase):
    def test_no_duplicated_emails(self):
        ''' Make sure there can't be duplicated emails in database '''

        customer1 = Customer(email='test@email.com')
        customer1.save()
        customer2 = Customer(email='test@email.com')
        with self.assertRaises(IntegrityError, msg='allows duplicated emails'):
            customer2.save()