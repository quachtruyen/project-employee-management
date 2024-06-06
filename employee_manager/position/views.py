from django.shortcuts import render
from .models import employee as employee_model
from .forms import EmployeeForm
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
"""hàm lấy danh sách nhân viên"""
def get_employee(request, offset):
    employee_list = employee_model.objects.filter().order_by('emp_id')[offset:offset+20]
    return render(request, 'employee/employee.html', {'employee_list' : employee_list})

"""hàm lấy thông tin nhân viên theo id"""
def get_employee_by_id(request, id):
    employee = employee_model.objects.get(emp_id = id)
    return render(request, 'employee/employee_detail.html', {'employee': employee})

"""hàm thêm nhân viên"""
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')  # Chuyển hướng sau khi lưu thành công
    else:
        form = EmployeeForm()
    return render(request, 'employee/add_employee_form.html', {'form': form})

"""hàm cập nhật nhân viên"""
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
from django.db.models import Q

"""hàm tìm kiếm nhân viên"""
def search_by_full_name_employee(request, model, field_name):
  """
  Hàm tìm kiếm các đối tượng trong model theo ký tự.

  Args:
    request: Đối tượng HttpRequest chứa dữ liệu truy vấn.
    model: Model Django mà bạn muốn tìm kiếm.
    field_name: Tên trường trong model mà bạn muốn tìm kiếm.

  Returns:
    Danh sách các đối tượng trong model khớp với truy vấn tìm kiếm.
  """

  search_query = request.GET.get('search_query')
  if search_query:
    # Lọc các đối tượng trong model có chứa ký tự tìm kiếm trong trường được chỉ định.
    objects = model.objects.filter(
      Q(**{field_name + '__contains': search_query})
    )
  else:
    # Lấy tất cả các đối tượng trong model nếu không có truy vấn tìm kiếm.
    objects = model.objects.all()

  return objects
 