from django.test import TestCase
from .forms.messageForm import MessageForm
from .forms.customerForm import CustomerForm

class TestForms(TestCase):
    def test_non_empty(self):
        form = MessageForm()
        self.assertFalse(form.is_valid())
        form = CustomerForm()
        self.assertFalse(form.is_valid())

    def test_valid_data(self):
        form_data = {
            'subject': 'test subject',
            'message': 'test message'
        }
        form = MessageForm(form_data)
        self.assertTrue(form.is_valid())


