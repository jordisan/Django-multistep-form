from django.http import HttpResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.shortcuts import redirect

from ..forms.messageForm import MessageForm
from ..forms.customerForm import CustomerForm
from ..forms.surveyForm import SurveyForm

from general.models.customer import Customer

SESSIONKEY_PREFIX = 'multistepform_step_'

STEPS = {
    1: {
        'form': 'SurveyForm'
    },
    2: {
        'form': 'MessageForm'
    },
    3:  {
        'form': 'CustomerForm'
    }
}

def __getSessionData(request, step):
    ''' Get session data for a step '''
    return request.session.get(SESSIONKEY_PREFIX + str(step))

def __getFormData(request, step):
    ''' Get form data stored in session, or empty otherwise '''
    return globals()[STEPS[step]['form']](__getSessionData(request, step))

def __setFormData(request, step, data):
    ''' Store form data in session '''
    request.session[SESSIONKEY_PREFIX + str(step)] = data

def __getNextStep(request):
    ''' Try to get first step not completed by user '''
    for i in range(1, len(STEPS)):
        if  __getSessionData(request, i) == None:
            return i
    return len(STEPS) # there's data in all steps => go to last step


def FormView(request, step):
    ''' View for multiple steps form '''

    if step == None:
        # no step in url => check previously stored data and redirect to non-completed step
        step = __getNextStep(request)
        return redirect('/step/' + str(step))

    form = globals()[STEPS[step]['form']]() # default form for current step

    if request.method == 'POST':
        if step == len(STEPS):
            # last step => save in database

            form = globals()[STEPS[step]['form']](request.POST)
            # check that user is not already on the database
            if form.is_valid():
                existing_customers = Customer.objects.filter(email=form.instance.email)
                if existing_customers.count() > 0:
                    # customer already exists => update data
                    existing_customer = existing_customers[0]
                    existing_customer.first_name = form.instance.first_name
                    existing_customer.last_name = form.instance.last_name
                    existing_customer.phone_number = form.instance.phone_number
                    form.instance = existing_customer
                    form.instance.save()
                else:
                    form.save() # save new customer

                # retrieve previous forms (stored in session) and save them
                for i in range(1, len(STEPS)):
                    form_stored = __getFormData(request, i)
                    form_stored.instance.customer = form.instance # set saved customer in related entities
                    form_stored.save()

                request.session.flush() # remove session data
                return render(request, 'multistepform/feedback.html', {
                    'page_title': 'Thanks',
                    'msg': 'Your data has been saved. We will contact you soon.'
                })

        else:
            # not last step => store data in session (temporarily) using model_to_dict to make it serializable

            form = globals()[STEPS[step]['form']](request.POST)
            if form.is_valid():
                __setFormData(request, step, model_to_dict(form.instance))
                return redirect('/step/' + str(step + 1))

    else:
        # GET => try to get data from session (in case it was previously stored)
        form = __getFormData(request, step)  

    return render(request, 'multistepform/form.html', {
        'page_title': 'Multiple steps form (' + str(step) + '/' + str(len(STEPS)) + ')',
        'form': form,
        'step': step,
        'step_last': len(STEPS)
    })