from django import forms
from .models import department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = department
        fields = ['name', 'description']
