# import base64
# import datetime
# import pyotp
# from django.shortcuts import render, redirect
# from django.views.decorators.csrf import csrf_exempt
# from .forms import Create_form_patient
# from django.contrib import messages
# from django.core.mail import EmailMultiAlternatives
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import authenticate, login
# from django.template.loader import get_template
# from django.contrib.auth.hashers import make_password, check_password
# import uuid
# from django.utils.html import escape
# from django.core.mail import send_mail
# from django.core.mail import send_mail
# from django.contrib.auth.models import User as off_user
# from .models import Patient
# from django.conf import settings
# User = settings.AUTH_USER_MODEL
# # Create your views here.
# @csrf_exempt
# @login_required(login_url='admin_login')
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def admin_dashboard(request):
#     # admin = Admin_Information.objects.get(user_id=pk)
#     if request.user.is_hospital_admin:
#         user = Admin_Information.objects.get(user=request.user)
#         total_patient_count = Patient.objects.annotate(count=Count('patient_id'))
#         total_doctor_count = Doctor_Information.objects.annotate(count=Count('doctor_id'))
#         total_pharmacist_count = Pharmacist.objects.annotate(count=Count('pharmacist_id'))
#         total_hospital_count = Hospital_Information.objects.annotate(count=Count('hospital_id'))
#         total_labworker_count = Clinical_Laboratory_Technician.objects.annotate(count=Count('technician_id'))
#         pending_appointment = Appointment.objects.filter(appointment_status='pending').count()
#         doctors = Doctor_Information.objects.all()
#         patients = Patient.objects.all()
#         hospitals = Hospital_Information.objects.all()
#         lab_workers = Clinical_Laboratory_Technician.objects.all()
#         pharmacists = Pharmacist.objects.all()
        
#         sat_date = datetime.date.today()
#         sat_date_str = str(sat_date)
#         sat = sat_date.strftime("%A")

#         sun_date = sat_date + datetime.timedelta(days=1) 
#         sun_date_str = str(sun_date)
#         sun = sun_date.strftime("%A")
        
#         mon_date = sat_date + datetime.timedelta(days=2) 
#         mon_date_str = str(mon_date)
#         mon = mon_date.strftime("%A")
        
#         tues_date = sat_date + datetime.timedelta(days=3) 
#         tues_date_str = str(tues_date)
#         tues = tues_date.strftime("%A")
        
#         wed_date = sat_date + datetime.timedelta(days=4) 
#         wed_date_str = str(wed_date)
#         wed = wed_date.strftime("%A")
        
#         thurs_date = sat_date + datetime.timedelta(days=5) 
#         thurs_date_str = str(thurs_date)
#         thurs = thurs_date.strftime("%A")
        
#         fri_date = sat_date + datetime.timedelta(days=6) 
#         fri_date_str = str(fri_date)
#         fri = fri_date.strftime("%A")
        
#         sat_count = Appointment.objects.filter(date=sat_date_str).filter(Q(appointment_status='pending') | Q(appointment_status='confirmed')).count()
#         sun_count = Appointment.objects.filter(date=sun_date_str).filter(Q(appointment_status='pending') | Q(appointment_status='confirmed')).count()
#         mon_count = Appointment.objects.filter(date=mon_date_str).filter(Q(appointment_status='pending') | Q(appointment_status='confirmed')).count()
#         tues_count = Appointment.objects.filter(date=tues_date_str).filter(Q(appointment_status='pending') | Q(appointment_status='confirmed')).count()
#         wed_count = Appointment.objects.filter(date=wed_date_str).filter(Q(appointment_status='pending') | Q(appointment_status='confirmed')).count()
#         thurs_count = Appointment.objects.filter(date=thurs_date_str).filter(Q(appointment_status='pending') | Q(appointment_status='confirmed')).count()
#         fri_count = Appointment.objects.filter(date=fri_date_str).filter(Q(appointment_status='pending') | Q(appointment_status='confirmed')).count()

#         context = {'admin': user,'total_patient_count': total_patient_count,'total_doctor_count':total_doctor_count,'pending_appointment':pending_appointment,'doctors':doctors,'patients':patients,'hospitals':hospitals,'lab_workers':lab_workers,'total_pharmacist_count':total_pharmacist_count,'total_hospital_count':total_hospital_count,'total_labworker_count':total_labworker_count,'sat_count': sat_count, 'sun_count': sun_count, 'mon_count': mon_count, 'tues_count': tues_count, 'wed_count': wed_count, 'thurs_count': thurs_count, 'fri_count': fri_count, 'sat': sat, 'sun': sun, 'mon': mon, 'tues': tues, 'wed': wed, 'thurs': thurs, 'fri': fri, 'pharmacists': pharmacists}
#         return render(request, 'hospital_admin/admin-dashboard.html', context)
#     elif request.user.is_labworker:
#         # messages.error(request, 'You are not authorized to access this page')
#         return redirect('labworker-dashboard')

# @csrf_exempt
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def admin_login(request):
#     if request.method == 'GET':
#         return render(request, 'hospital_admin/login.html')
#     elif request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         try:
#             user = User.objects.get(username=username)
#         except:
#             messages.error(request, 'Username does not exist')

#         user = authenticate(username=username, password=password)

#         if user is not None:
#             login(request, user)
#             if user.is_hospital_admin:
#                 messages.success(request, 'User logged in')
#                 return redirect('admin-dashboard')
#             elif user.is_labworker:
#                 messages.success(request, 'User logged in')
#                 return redirect('labworker-dashboard')
#             elif user.is_pharmacist:
#                 messages.success(request, 'User logged in')
#                 return redirect('pharmacist-dashboard')
#             else:
#                 return redirect('admin-logout')
#         else:
#             messages.error(request, 'Invalid username or password')
        

#     return render(request, 'hospital_admin/login.html')


# @csrf_exempt
# def admin_register(request):
#     page = 'hospital_admin/register'
#     form = AdminUserCreationForm()

#     if request.method == 'POST':
#         form = AdminUserCreationForm(request.POST)
#         if form.is_valid():
#             # form.save()
#             # commit=False --> don't save to database yet (we have a chance to modify object)
#             user = form.save(commit=False)
#             user.is_hospital_admin = True
#             user.save()

#             messages.success(request, 'User account was created!')
            
#             # After user is created, we can log them in
#             #login(request, user)
#             return redirect('admin_login')

#         else:
#             messages.error(request, 'An error has occurred during registration')

#     context = {'page': page, 'form': form}
#     return render(request, 'hospital_admin/register.html', context)