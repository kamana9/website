from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=30)
    sid=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Student" 
        verbose_name_plural="Students"

class Teacher(models.Model):
    name=models.CharField(max_length=10)
    subject=models.CharField(max_length=10)        
    
