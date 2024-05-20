from django.shortcuts import render
from .models import department as department_model
from django.shortcuts import render, get_object_or_404

# Create your views here.
def get_department(request):
    department_list = department_model.objects.filter().order_by('department_id')
    return render(request, 'department/department.html', {'department_list' : department_list})

def get_department_by_id(request, department_id):
    department = get_object_or_404(department_model, department_id=department_id)
    return render(request, 'department/department_detail.html', {'department': department})