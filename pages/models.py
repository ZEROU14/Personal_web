from django.db import models

# Create your models here.
class Question(models.Model):
    Full_name = models.CharField(max_length=500)
    Email = models.EmailField(max_length=253)
    Subject = models.CharField(max_length=100)
    Message = models.TextField()

    def __str__(self):
        return (f'Name = {self.Full_name}, Subject ={self.Subject}')

class Client(models.Model):
    logo = models.ImageField(upload_to='clients/')


class TitleOne(models.Model):
    title = models.TextField()


class WhatIdo(models.Model):
    icon = models.CharField(max_length= 500,blank=True ,help_text='pls visit this site   https://linearicons.com/free    to get icon')
    # visit https://linearicons.com/free this site for icon
    title = models.CharField(max_length=200,blank=True)
    description = models.TextField()