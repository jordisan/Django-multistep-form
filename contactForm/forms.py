from django import forms 
from .models import customer 
  

class ContactForm(forms.ModelForm): 
    class Meta: 
        model = customer.Customer 
        fields = "__all__"