import email
from django.contrib import admin
from .models import *

# Register your models here.


class Useradmin(admin.ModelAdmin):
    model = User
    list_display=['username','password']


admin.site.register(User,Useradmin)
