from django.db import models
# from django.contrib.auth.models import User
from user.models import User
from django.conf import settings
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mob = models.IntegerField()

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='patient')
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    # featured_image = models.ImageField(upload_to='patients/', default='patients/user-default.png', null=True, blank=True)
    blood_group = models.CharField(max_length=200, null=True, blank=True)
    history = models.CharField(max_length=200, null=True, blank=True)
    dob = models.CharField(max_length=200, null=True, blank=True)
    nid = models.CharField(max_length=200, null=True, blank=True)
    serial_number = models.CharField(max_length=200, null=True, blank=True)
    
    # Chat
    login_status = models.CharField(max_length=200, null=True, blank=True, default="offline")

    def __str__(self):
        return str(self.user.username)