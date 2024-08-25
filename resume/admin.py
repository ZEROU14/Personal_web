from django.contrib import admin

# Register your models here.
from .models import Experience,Knowledge,Certificates

admin.site.register(Experience)
admin.site.register(Knowledge)
admin.site.register(Certificates)