from django.contrib import admin

# Register your models here.
from main.models import *
 
admin.site.register(Categories)
admin.site.register(Meals)


