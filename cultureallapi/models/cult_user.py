from xmlrpc.client import boolean
from django.db import models
from django.contrib.auth.models import User

class CultUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    terms_signed = models.BooleanField(default=False)