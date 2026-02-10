from django.db import models
from datetime import datetime
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=20)
   
    def __str__(self):
        return self.name