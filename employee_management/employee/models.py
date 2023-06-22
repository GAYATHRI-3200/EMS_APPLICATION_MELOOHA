from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    position = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
