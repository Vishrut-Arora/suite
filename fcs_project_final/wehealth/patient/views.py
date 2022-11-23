import base64
import datetime
import pyotp
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import Create_form_patient
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.template.loader import get_template
from django.contrib.auth.hashers import make_password, check_password
import uuid
from django.utils.html import escape
from django.core.mail import send_mail
from django.core.mail import send_mail
from django.contrib.auth.models import User as off_user
from .models import Patient
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your views here.
@csrf_exempt
def patient_login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('patient_dashboard')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'patient_login.html', {'form':form, 'title':'log in'})

@csrf_exempt
def patient_register(request):
    print("ok")
    if request.method == 'POST':
        print("ok")
        form = Create_form_patient(request.POST)
        #print(request.POST)
        if form.is_valid():
            # pswd = make_password(str(form.cleaned_data['password1']))
            print("ok")
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            pswd = form.cleaned_data.get('password1')
            print(username,email,pswd)
            print(request.POST)
            ######################### mail system ####################################
            htmly = get_template('Email.html')
            my_uuid = uuid.uuid4()
            check_otp = '2@33$6%5'
            d = { 'otp': check_otp }
            print("otp",check_otp)
            send_mail(subject = 'OTP to Register',message = check_otp,from_email = 'eshumanohare@gmail.com',recipient_list=[email])
            print("Not saved")
            user = form.save(commit=False)
            user.is_patient=True
            user.save()
            print("saved")
            ##################################################################
            return render(request=request, template_name='patient_otp.html',context={'email': email, 'password1':pswd,'username':username, 'form':form})
        else:
            form = Create_form_patient()

    else:
        form = Create_form_patient()
    return render(request, 'patient_register.html', {'form': form, 'title':'register here'})


@csrf_exempt
def patient_otp(request):
    print("okk jiji")
    print(request.POST)
    if request.method=='POST':
        password = escape(request.POST.get('password1'))
        username = escape(request.POST.get('username'))
        email = escape(request.POST.get('email'))

        otp = escape(request.POST.get('otp'))
        form = escape(request.POST.get('form'))
        print(form)
        # print(otp)
        # keygen = generateKey()
        # key = base64.b32encode(keygen.returnValue("vishrut.company@gmail.com").encode())
        # OTP = pyotp.TOTP(key,interval = 400)
        # print(OTP.now())
        # if OTP.verify(otp):
        print(username ,password ,email)
        if(otp=="2@33$6%5"):
            print("correct:", otp)
            print(request.POST)
            messages.success(request, "Registration successful." )
            return redirect("patient_login")
        else:
            messages.error(request, "Unsuccessful registration. Invalid OTP.")
            return redirect("home")
    else:
        return render(request=request, template_name='patient_otp.html')

@csrf_exempt
def patient_dashboard(request):
    print("ok dashboard")
    if request.User.is_patient:
        # patient = Patient.objects.get(user_id=pk)
        patient = Patient.objects.get(user=request.User)
        report = Report.objects.filter(patient=patient)
        prescription = Prescription.objects.filter(patient=patient).order_by('-prescription_id')
        appointments = Appointment.objects.filter(patient=patient).filter(Q(appointment_status='pending') | Q(appointment_status='confirmed'))
        # payments = Payment.objects.filter(patient=patient).filter(appointment__in=appointments).filter(payment_type='appointment').filter(status='VALID')
        payments=' '
        context = {'patient': patient, 'appointments': appointments, 'payments': payments,'report':report,'prescription':prescription}
    else:
        return redirect('logout')
    return render(request,'patient_dashboard.html')

@csrf_exempt
class generateKey:
	@staticmethod
	def returnValue(phone):
		return str(phone) + "Random Secret Key nice"

@csrf_exempt
def patient_dashboard(request):
    return render(request,'patient_dashboard.html')