from django.contrib import admin
from general.models.customer import Customer
from .models.contactMessage import ContactMessage

# Register your models here.
admin.site.register(Customer)
admin.site.register(ContactMessage)
