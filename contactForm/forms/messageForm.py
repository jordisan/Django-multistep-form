from django import forms 
from general.models.customer import Customer 
from ..models.contactMessage import ContactMessage

class MessageForm(forms.ModelForm): 
    class Meta: 
        model = ContactMessage
        exclude = ('customer',) # we will assign it from CustomerForm
        widgets = {
            'message': forms.Textarea(),
        }
