from django.db import models
from general.models.base import Base
from general.models.customer import Customer

class FormMessage(Base):
    """ Message from customer """

    subject = models.CharField(max_length=30)
    message = models.CharField(max_length=500)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='email')
