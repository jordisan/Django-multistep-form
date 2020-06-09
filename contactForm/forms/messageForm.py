from django import forms 
from general.models.customer import Customer 
from ..models.contactMessage import ContactMessage

class MessageForm(forms.ModelForm): 
    class Meta: 
        model = ContactMessage
        fields = "__all__"
        widgets = {
            'message': forms.Textarea(),
        }
