from myapp1.models import Patient
from django import forms

class PatientSignupForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields='__all__'