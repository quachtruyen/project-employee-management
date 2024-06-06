from django.db import models
from datetime import date

# Create your models here.
class department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=200)
    description = models.CharField(null=True, max_length=2000)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.department_id}, {self.name}, {self.create_date}"