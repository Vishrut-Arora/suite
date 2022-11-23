from django.contrib.auth.forms import UserCreationForm
from django import forms
from user.models import User
from .models import Patient

class Create_form_patient(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'phone_number', 'blood_group', 'history', 'nid', 'dob', 'address']

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})