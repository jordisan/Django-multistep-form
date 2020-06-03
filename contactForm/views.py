from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'contactForm/page1.html', {
        'page_title': 'Page 1',
        'page_content': 'Hello, Django!',
    })