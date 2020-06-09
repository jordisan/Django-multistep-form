from django.db import models
from .person import Person
from phonenumber_field.modelfields import PhoneNumberField

class Customer(Person):
    """ Customer (existing or future) """

    email = models.EmailField()
    phone_number = models.CharField(max_length=20) # PhoneNumberField()