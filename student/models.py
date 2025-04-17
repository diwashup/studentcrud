from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=100)
    student_contact= models.CharField(max_length=100)   
    student_email = models.EmailField(max_length=100)
    student_address = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name