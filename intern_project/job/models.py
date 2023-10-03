from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    reward = models.PositiveIntegerField()
    content = models.TextField()
    technology = models.CharField(max_length=100)

class Applying(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)