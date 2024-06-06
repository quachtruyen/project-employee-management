from django.contrib import admin
from .models import employee

# Register your models here.
class employeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'department_id', 'full_name', 'create_date', 'date_of_birth')
    list_filter = ('department_id', 'full_name', 'create_date', 'date_of_birth')
    search_fields = ['emp_id', 'department_id', 'full_name', 'create_date', 'date_of_birth']
admin.site.register(employee)