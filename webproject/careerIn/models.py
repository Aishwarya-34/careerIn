from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Resumes(models.Model):
    name = models.CharField(max_length=300)
    cgpa = models.FloatField(null=True)
    college = models.CharField(max_length=300,null=True)
    primary_education = models.CharField(max_length=300,null=True)
    secondary_education = models.CharField(max_length=300,null=True)
    degree = models.CharField(max_length=100,null=True)
    looking_up = models.CharField(max_length=100,null=True)
    key_skills = ArrayField(models.CharField(max_length=10, blank=True),size=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='resumes',on_delete=models.CASCADE)

class bookmark(models.Model):
    name = models.CharField(max_length=300)
    link = models.CharField(max_length=500)
    last_data = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Aishwarya - Create the Contact us database model here.Refer how its done above
    

