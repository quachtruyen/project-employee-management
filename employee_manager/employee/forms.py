from django import forms
from .models import employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = ['department', 'position', 'full_name', 'date_of_birth', 'sex', 'address', 'phone_number', 'email', 'date_join_company', 'academic_level', 'work_experience', 'marital_status', 'identification_card', 'card_photo']