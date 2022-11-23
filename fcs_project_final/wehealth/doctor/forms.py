from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class Create_form_doctor(UserCreationForm):
    class Meta:
        email = forms.EmailField()
        # phone_no = forms.CharField(max_length = 10)
        first_name = forms.CharField(max_length = 20)
        last_name = forms.CharField(max_length = 20)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']