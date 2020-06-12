from django.conf import settings
from django.urls import path
from contactForm.views.contactView import ContactView
from contactForm.views.cancelView import CancelView

urlpatterns = [
    path('', ContactView, {'step': 1}),
    path('step/<int:step>', ContactView),
    path('cancel', CancelView),
]

if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL,
    #                       document_root=settings.MEDIA_ROOT)