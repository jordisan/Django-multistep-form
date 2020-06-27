from django import forms 
from general.models.customer import Customer 
from ..models.formMessage import FormMessage

class MessageForm(forms.ModelForm): 
    class Meta: 
        model = FormMessage
        exclude = ('customer',) # we will assign it from CustomerForm
        widgets = {
            'additional_message': forms.Textarea(),
        }
