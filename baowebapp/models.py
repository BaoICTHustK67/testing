from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.BigAutoField(primary_key=True, db_index=False)
    name = models.CharField(max_length=50, null=True)
    gender = models.IntegerField(null=True)
    school = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.name}'