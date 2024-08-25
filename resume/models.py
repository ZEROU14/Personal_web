from django.db import models

# Create your models here.
class Experience(models.Model):
    company = models.CharField(max_length=100,blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    start_date = models.CharField(max_length=12)
    end_date = models.CharField(max_length=12)
    

class Certificates(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    logo = models.ImageField(upload_to='Certificates/',blank=True)


class Knowledge(models.Model):
    title = models.CharField(max_length=100)