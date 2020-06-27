from django.contrib import admin
from general.models.customer import Customer
from .models.formMessage import FormMessage

# Register your models here.
admin.site.register(Customer)
admin.site.register(FormMessage)
