from django.contrib import admin
from account import models

# Register your models here.

admin.site.register(models.Account)
admin.site.register(models.Professor)
admin.site.register(models.Student)