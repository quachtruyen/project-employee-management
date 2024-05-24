from django.shortcuts import render
from .models import department as department_model
from django.shortcuts import render, get_object_or_404
from employee.models import employee as employee_model

# Create your views here.
def get_department(request):
    department_list = department_model.objects.filter().order_by('department_id')
    return render(request, 'department/department.html', {'department_list' : department_list})

def get_department_by_id(request, id):
    employee_list = employee_model.objects.filter(department_id = id)
    department = department_model.objects.get(department_id = id)
    return render(request, 'department/department_detail.html', {'employee_list': employee_list,'department': department})