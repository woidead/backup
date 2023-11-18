from django.db import models

# Create your models here.


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_add = models.DateField(auto_now=True)
    time_update = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True) 
    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    def __str__(self):
        return self.name
    