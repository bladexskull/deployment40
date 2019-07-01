from django.contrib import admin

# Register your models here.

from modellearning.models import Locationdata,Jobdata,Personname

admin.site.register(Locationdata)
admin.site.register(Jobdata)
admin.site.register(Personname)
