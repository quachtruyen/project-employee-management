from django import forms
from .models import employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = ['department', 'position', 'first_name', 'last_name', 'full_name', 'age', 'date_of_birth']