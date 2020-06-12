from django.http import HttpResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.shortcuts import redirect

from ..forms.messageForm import MessageForm
from ..forms.customerForm import CustomerForm

def ContactView(request, step=1):
    ''' View for contact form; step 1 is for message; step 2 is for customer data'''
    
    SESSIONKEY_DATA_MESSAGE = 'contact_message'
    SESSIONKEY_DATA_CUSTOMER = 'contact_customer'
    STEP_LAST = 2

    form = None
    if step == 2:
        form = CustomerForm()
    else:
        form = MessageForm()

    if request.method == 'POST':
        if step == STEP_LAST:
            # save in database
            form = CustomerForm(request.POST)
            if form.is_valid():
                request.session[SESSIONKEY_DATA_CUSTOMER] = model_to_dict(form.instance)
                # ToDo: save data (message and custom info)

        else:
            # store data in session (temporarily) using model_to_dict to make it serializable
            form = MessageForm(request.POST)
            if form.is_valid():
                request.session[SESSIONKEY_DATA_MESSAGE] = model_to_dict(form.instance)
                return redirect('/step/' + str(step + 1))

    else:
        # try to get data from session (if it was previously stored)
        if step == 2:
            form =  CustomerForm(request.session.get(SESSIONKEY_DATA_CUSTOMER))    
        else:
            form =  MessageForm(request.session.get(SESSIONKEY_DATA_MESSAGE))    

    return render(request, 'contactForm/contact.html', {
        'page_title': 'Contact form (' + str(step) + '/' + str(STEP_LAST) + ')',
        'form': form,
        'step': step,
        'step_last': STEP_LAST
    })