from django import forms 
from general.models.customer import Customer 
  

class ContactForm(forms.ModelForm): 
    class Meta: 
        model = Customer 
        fields = "__all__"