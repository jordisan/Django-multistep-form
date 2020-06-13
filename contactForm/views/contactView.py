from django.http import HttpResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.shortcuts import redirect

from ..forms.messageForm import MessageForm
from ..forms.customerForm import CustomerForm

from general.models.customer import Customer

def ContactView(request, step=1):
    ''' View for contact form; step 1 is for message; step 2 is for customer data'''
    
    SESSIONKEY_DATA_MESSAGE = 'contact_message'
    SESSIONKEY_DATA_CUSTOMER = 'contact_customer'
    STEP_LAST = 2

    form = None
    if step == STEP_LAST:
        form = CustomerForm()
    else:
        form = MessageForm()

    if request.method == 'POST':
        if step == STEP_LAST:
            # save in database
            form = CustomerForm(request.POST)
            if form.is_valid():
                # check that user is not already on the database
                if not Customer.objects.filter(email=form.instance.email).exists() :
                    form.save() # save customer data if new; TODO: should we update data if customer already exists?

                form_m = MessageForm(request.session.get(SESSIONKEY_DATA_MESSAGE)) # retrieve message from session
                form_m.instance.customer = form.instance
                form_m.save() # save message data
                request.session.flush() # remove session data
                return render(request, 'contactForm/feedback.html', {
                    'page_title': 'Thanks',
                    'msg': 'Your data has been saved. We will contact you soon.'
                })

        else:
            # not last step => store data in session (temporarily) using model_to_dict to make it serializable
            form = MessageForm(request.POST)
            if form.is_valid():
                request.session[SESSIONKEY_DATA_MESSAGE] = model_to_dict(form.instance)
                return redirect('/step/' + str(step + 1))

    else:
        # try to get data from session (in case it was previously stored)
        if step == STEP_LAST:
            form =  CustomerForm(request.session.get(SESSIONKEY_DATA_CUSTOMER))    
        else:
            form =  MessageForm(request.session.get(SESSIONKEY_DATA_MESSAGE))    

    return render(request, 'contactForm/contact.html', {
        'page_title': 'Contact form (' + str(step) + '/' + str(STEP_LAST) + ')',
        'form': form,
        'step': step,
        'step_last': STEP_LAST
    })