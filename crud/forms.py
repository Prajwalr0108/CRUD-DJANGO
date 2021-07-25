from django import forms
from django.forms import fields
from .models import BasicDetails, Education

class BasicDetailsForm(forms.ModelForm):
    class Meta:
        model = BasicDetails
        fields = '__all__'

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
