from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

