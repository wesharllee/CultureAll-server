from django.db import models

class ContactRequest(models.Model):
    email = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    contact_by_phone = models.BooleanField()