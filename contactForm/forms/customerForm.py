from django import forms 
from general.models.customer import Customer 

class CustomerForm(forms.ModelForm):
    class Meta: 
        model = Customer 
        fields = ['email', 'first_name', 'last_name', 'phone_number']

    def validate_unique(self):
        '''
        Do not check uniqueness of email address here as we want to allow existing emails
        to add new messages; we will do it at the view.
        This is not a 'new customer' form, but a form to provide customer data to the message.
        '''
        pass