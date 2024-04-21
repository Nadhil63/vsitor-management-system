from django.contrib.auth.models import User
from django.db import models

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    office_location = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    class Meta:
        app_label = 'api'

class VisitorLog(models.Model):
    visitor_name = models.CharField(max_length=100)
    visitor_email = models.EmailField()
    visiting_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    office_location = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    class Meta:
        app_label = 'api'
