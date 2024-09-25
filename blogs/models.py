from django.db import models
from django.shortcuts import reverse
from ckeditor.fields import RichTextField
# from ckeditor.fields import CKEditorField
# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to='Blogs_cover/', blank= True)

    def get_absolute_url(self):
        return reverse("blog_info", args=[self.pk])
    
