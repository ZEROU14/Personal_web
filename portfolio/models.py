from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=100,blank=True)
    cover = models.ImageField(upload_to='Portfolio/',)
    url = models.URLField(max_length=200)