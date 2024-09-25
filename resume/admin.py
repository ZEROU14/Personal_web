from django.contrib import admin

# Register your models here.
from .models import Experience,Knowledge,Certificates,Design,Coding,Education

admin.site.register(Experience)
admin.site.register(Knowledge)
admin.site.register(Certificates)
admin.site.register(Design)
admin.site.register(Coding)
admin.site.register(Education)
