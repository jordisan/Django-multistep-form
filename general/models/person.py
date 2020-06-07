from django.db import models
from .base import Base

class Person(Base):
    """ Any real person """

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)