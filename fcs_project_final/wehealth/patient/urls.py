from django.urls import path
from . import views

# from . --> same directory
# Views functions and urls must be linked. # of views == # of urls
# App URL file - urls related to hospital

urlpatterns = [
    path('patient_login/', views.patient_login, name='patient_login'),
    path('patient_login/patient_dashboard',views.patient_dashboard, name='patient_dashboard'),
    path('patient_register/',views.patient_register, name='patient_register'),
    path('patient_register/patient_otp',views.patient_otp, name='patient_otp'),
]