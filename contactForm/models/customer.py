from django.db import models
from .person import Person

class Customer(Person):
    """ Customer (existing or future) """

    email = models.EmailField()