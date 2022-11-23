from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_hospital_admin = models.BooleanField(default=False)
    is_labworker = models.BooleanField(default=False)
    is_pharmacist = models.BooleanField(default=False)
    #login_status = models.CharField(max_length=200, null=True, blank=True, default="offline")
    login_status = models.BooleanField(default=False)