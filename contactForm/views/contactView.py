from django.http import HttpResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.shortcuts import redirect

from ..forms.messageForm import MessageForm
from ..forms.customerForm import CustomerForm

from general.models.customer import Customer

def ContactView(request, step=1):
    ''' View for contact form; step 1 is for message; step 2 is for customer data'''
    
    STEPS = {
        1: {
            'form': 'MessageForm'
        },
        2:  {
            'form': 'CustomerForm'
        }
    }
    
    SESSIONKEY_PREFIX = 'contactform_step_'

    form = globals()[STEPS[step]['form']]()

    if request.method == 'POST':
        if step == len(STEPS):
            # last step => save in database
            form = globals()[STEPS[step]['form']](request.POST)
            # check that user is not already on the database
            if form.is_valid():
                if not Customer.objects.filter(email=form.instance.email).exists():
                    form.save() # save customer data if new; TODO: should we update data if customer already exists?
                else:
                    form_m = globals()[STEPS[1]['form']](request.session.get(SESSIONKEY_PREFIX + '1')) # retrieve message (first step) from session
                    form_m.instance.customer = form.instance
                    form_m.save() # save message data
                    request.session.flush() # remove session data
                    return render(request, 'contactForm/feedback.html', {
                        'page_title': 'Thanks',
                        'msg': 'Your data has been saved. We will contact you soon.'
                    })

        else:
            # not last step => store data in session (temporarily) using model_to_dict to make it serializable
            form = globals()[STEPS[step]['form']](request.POST)
            if form.is_valid():
                request.session[SESSIONKEY_PREFIX + str(step)] = model_to_dict(form.instance)
                return redirect('/step/' + str(step + 1))

    else:
        # try to get data from session (in case it was previously stored)
        form = globals()[STEPS[step]['form']](request.session.get(SESSIONKEY_PREFIX + str(step)))  

    return render(request, 'contactForm/contact.html', {
        'page_title': 'Contact form (' + str(step) + '/' + str(len(STEPS)) + ')',
        'form': form,
        'step': step,
        'step_last': len(STEPS)
    })