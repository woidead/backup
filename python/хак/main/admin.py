from django.contrib import admin

from main.models import Cross

# Register your models here.

class CrossAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'desc', 'category']

admin.site.register(Cross, CrossAdmin)