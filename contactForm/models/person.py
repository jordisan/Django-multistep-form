from django.db import models


class Person(models.Model):
    """ Any real person """

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)