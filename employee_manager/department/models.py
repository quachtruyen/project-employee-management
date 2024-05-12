from django.db import models

# Create your models here.
class department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=200)

    def __str__(self):
        return f"{self.department_id}, {self.name}"