from django.conf import settings
from django.urls import path
from contactForm.views.contactMessage import ContactMessage

urlpatterns = [
    path("", ContactMessage, name="home"),
]

if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL,
    #                       document_root=settings.MEDIA_ROOT)