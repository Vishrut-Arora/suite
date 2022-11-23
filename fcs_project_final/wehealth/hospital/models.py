from django.db import models

# Create your models here.
class Hospital_Information(models.Model):
    # ('database value', 'display_name')
    HOSPITAL_TYPE = (
        ('private', 'Private hospital'),
        ('public', 'Public hospital'),
    )

    hospital_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    featured_image = models.ImageField(upload_to='hospitals/', default='hospitals/default.png', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    hospital_type = models.CharField(max_length=200, choices=HOSPITAL_TYPE)
    general_bed_no = models.IntegerField(null=True, blank=True)
    available_icu_no = models.IntegerField(null=True, blank=True)
    regular_cabin_no = models.IntegerField(null=True, blank=True)
    emergency_cabin_no = models.IntegerField(null=True, blank=True)
    vip_cabin_no = models.IntegerField(null=True, blank=True)

    # String representation of object
    def __str__(self):
        return str(self.name)