from django.db import models
from ckeditor.fields import RichTextField
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
    
    def __str__(self):
        return self.title
    

class Certificates(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    logo = models.ImageField(upload_to='Certificates/',blank=True)

    def __str__(self):
        return self.title


class Knowledge(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Design(models.Model):
    title = models.CharField(max_length=100)
    proficiency_in_number = models.IntegerField()

    def __str__(self):
        return self.title
    
class Coding(models.Model):
    title = models.CharField(max_length=100)
    proficiency_in_number = models.IntegerField()

    def __str__(self):
        return self.title
    
class Education(models.Model):
    title = RichTextField()
