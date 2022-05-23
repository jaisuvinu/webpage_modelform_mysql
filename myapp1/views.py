from django.shortcuts import render
from myapp1.forms import PatientSignupForm


def home(request):
    patient=PatientSignupForm()
    return render(request,'signin.html',{"patientform":patient})