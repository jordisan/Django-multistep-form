from django import forms 
from ..models.formSurvey import FormSurvey

CHOICES = ( (True,'Yes'),
            (False,'No'),
          )

class SurveyForm(forms.ModelForm): 
    are_you_happy = forms.TypedChoiceField(
                         choices=CHOICES, widget=forms.RadioSelect
                    )
    do_you_know_it = forms.TypedChoiceField(
                         choices=CHOICES, widget=forms.RadioSelect
                    )
    class Meta: 
        model = FormSurvey
        exclude = ('customer',) # we will assign it from CustomerForm

