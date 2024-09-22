from django.contrib import admin


from .models import Question,Client,TitleOne,WhatIdo
# Register your models here.

admin.site.register(Question)
admin.site.register(Client)
admin.site.register(TitleOne)
admin.site.register(WhatIdo)