from django.db import models
from .person import Person

class Customer(Person):
    """ Customer (existing or future) """

    email = models.EmailField(unique=True, db_index=True, primary_key=True)
    phone_number = models.CharField(max_length=20, blank=True) # PhoneNumberField()