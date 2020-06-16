from django.conf import settings


def custom_settings(request):
    return { 
        'API_URL': settings.API_URL
    }