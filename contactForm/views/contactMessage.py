from django.http import HttpResponse
from django.shortcuts import render

from ..forms.messageForm import MessageForm

def ContactMessage(request):
    return render(request, 'contactForm/contact1.html', {
        'page_title': 'Contact form (1/2)',
        'form': MessageForm(),
    })