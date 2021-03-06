from django.db import models
from general.models.base import Base
from general.models.customer import Customer

class FormMessage(Base):
    """ Message from customer """

    additional_message = models.CharField(max_length=500, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='email')
