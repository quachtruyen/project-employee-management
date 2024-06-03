from django.shortcuts import render
from .models import department as department_model
from django.shortcuts import render, get_object_or_404
from employee.models import employee as employee_model
from .forms import DepartmentForm
from django.shortcuts import render, redirect

# Create your views here.
def get_department(request):
    department_list = department_model.objects.filter().order_by('department_id')
    return render(request, 'department/department.html', {'department_list' : department_list})

def get_department_by_id(request, id):
    employee_list = employee_model.objects.filter(department_id = id)
    department = department_model.objects.get(department_id = id)
    return render(request, 'department/department_detail.html', {'employee_list': employee_list,'department': department})

def add_Department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')  # Chuyển hướng sau khi lưu thành công
    else:
        form = DepartmentForm()
    return render(request, 'department/add_department_form.html', {'form': form})