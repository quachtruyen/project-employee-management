from django.contrib import admin
from .models import department

# Register your models here.
class departmentAdmin(admin.ModelAdmin):
    list_display = ('department_id', 'name')
    search_fields = ['name']
    list_filter = ('department_id', 'name')
admin.site.register(department, departmentAdmin)