from django.db import models
from department.models import department
from position.models import position

# Create your models here.
class employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    department = models.ForeignKey(department, default=None, on_delete=models.CASCADE)
    position = models.ForeignKey(position, default=None, on_delete=models.CASCADE)
    full_name = models.CharField(null=False, max_length=200)
    date_of_birth = models.DateField(null=False)
    sex = models.CharField(null=False, max_length=20)
    address = models.CharField(null=False, max_length=2000)
    phone_number = models.CharField(null=False, max_length=10)
    email = models.CharField(null=False, max_length=200)
    date_join_company = models.DateTimeField(null=False)
    academic_level = models.CharField(null=True, max_length=200)
    work_experience = models.CharField(null=True, max_length=2000)
    marital_status = models.BooleanField()
    identification_card = models.CharField(null=False, max_length=20)
    card_photo = models.ImageField(upload_to='nhan_vien')
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.emp_id}, {self.full_name}, {self.date_of_birth}, {self.sex}, {self.address}, {self.phone_number}, {self.email}, {self.date_join_company}, {self.academic_level}, {self.work_experience}, {self.marital_status}, {self.identification_card}, {self.card_photo}, {self.create_date}"
    