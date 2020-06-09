from django.db import models
from general.models.base import Base

class ContactMessage(Base):
    """ Contact from customer """

    subject = models.CharField(max_length=30)
    message = models.CharField(max_length=500)
