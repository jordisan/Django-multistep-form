from django.test import TestCase
from .forms.messageForm import MessageForm
from .forms.customerForm import CustomerForm

class TestForms(TestCase):

    def test_non_empty(self):
        ''' Make sure empty forms aren't allowed '''

        form = MessageForm()
        self.assertFalse(form.is_valid(), msg='empty messages allowed')
        form = CustomerForm()
        self.assertFalse(form.is_valid(), msg='empty customer allowed')

    def test_valid_data(self):
        ''' Make sure valid data is accepted '''

        form_data = {
            'subject': 'test subject',
            'message': 'test message'
        }
        form = MessageForm(form_data)
        self.assertTrue(form.is_valid(), 'unable to validate message data')


