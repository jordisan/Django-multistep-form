from django.db import models
from general.models.base import Base
from general.models.customer import Customer

class FormSurvey(Base):
    """ Ask some questions """

    are_you_happy = models.BooleanField()
    do_you_know_it = models.BooleanField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='email')
