from django.conf import settings
from django.urls import path
from multistepform.views.formView import FormView
from multistepform.views.cancelView import CancelView

urlpatterns = [
    path('', FormView, {'step': 1}),
    path('step/<int:step>', FormView),
    path('cancel', CancelView),
]

if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL,
    #                       document_root=settings.MEDIA_ROOT)