from django.urls import path
from . import views


# from . --> same directory
# Views functions and urls must be linked. # of views == # of urls
# App URL file - urls related to hospital

urlpatterns = [
    path('doctor_login/', views.doctor_login, name='doctor_login'),
    path('doctor_login/doctor_dashboard',views.doctor_dashboard, name='doctor_dashboard'),
    path('doctor_register/',views.doctor_register, name='doctor_register'),
    path('doctor_register/doctor_otp',views.doctor_otp, name='doctor_otp'),
]