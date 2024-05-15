from django.db import models
from department.models import department
from position.models import position

# Create your models here.
class employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    department_id = models.ForeignKey(department, default=None, on_delete=models.CASCADE)
    position_id = models.ForeignKey(position, default=None, on_delete=models.CASCADE)
    first_name = models.CharField(null=False, max_length=100)
    last_name = models.CharField(null=False, max_length=100)
    full_name = models.CharField(null=False, max_length=200)
    age = models.IntegerField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateField()
    
    def __str__(self):
        return f"{self.emp_id}, {self.first_name}, {self.last_name}, {self.full_name}, {self.age}, {self.create_date}, {self.date_of_birth}"
    