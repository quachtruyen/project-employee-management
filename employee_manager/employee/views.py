from django.shortcuts import render
from .models import employee as employee_model
from .forms import EmployeeForm
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def get_employee(request):
    employee_list = employee_model.objects.filter().order_by('emp_id')
    return render(request, 'employee/employee.html', {'employee_list' : employee_list})

def get_employee_by_id(request, id):
    employee = employee_model.objects.get(emp_id = id)
    return render(request, 'employee/employee_detail.html', {'employee': employee})

def add_Department(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')  # Chuyển hướng sau khi lưu thành công
    else:
        form = EmployeeForm()
    return render(request, 'employee/add_employee_form.html', {'form': form})

def update_employee(request, emp_id):
    employee = get_object_or_404(employee_model, emp_id=emp_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Chuyển hướng đến danh sách nhân viên sau khi cập nhật
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update_employee.html', {'form': form})