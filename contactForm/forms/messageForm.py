from django import forms 
from general.models.customer import Customer 
from ..models.contact import Contact  

class MessageForm(forms.ModelForm): 
    class Meta: 
        model = Contact 
        fields = "__all__"
        widgets = {
            'message': forms.Textarea(),
        }
