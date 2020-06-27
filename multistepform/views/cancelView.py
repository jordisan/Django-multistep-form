from django.http import HttpResponse
from django.shortcuts import render

def CancelView(request):
    ''' View after finishing process '''
    # remove all data stored in session
    request.session.flush()
    return render(request, 'multistepform/feedback.html', {
        'page_title': 'Cancelled',
        'msg': 'Your data has been removed. Thanks.'
    })

 