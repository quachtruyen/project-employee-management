from django.db import models
from employee.models import employee

# Create your models here.
class salary(models.Model):
    salary_id = models.AutoField(primary_key=True)
    month = models.DateField()
    emp_id = models.ForeignKey(employee, default=None, on_delete=models.CASCADE)
    basic_salary = models.FloatField()
    coefficients_salary = models.IntegerField()
    allowance = models.FloatField()
    total_income = models.FloatField()
    personal_income_tax = models.FloatField()
    amount_actually_received = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.position_id}, {self.name}, {self.create_date}"