from django.shortcuts import render

# Create your views here.
def hospital_home(request):
    content = {}
    return render(request, 'index.html', content)