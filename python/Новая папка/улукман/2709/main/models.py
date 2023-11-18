from tabnanny import verbose
from unicodedata import category
from django.db import models
class Categories(models.Model):
    title = models.CharField(max_length = 30, verbose_name = 'Название')
    def __str__(self):
        return self.title
        
# Create your models here.
class Meals(models.Model):
    title = models.CharField(max_length = 250, verbose_name = 'Название')
    discription =  models.TextField( verbose_name = 'описание')
    image = models.ImageField(upload_to = 'core', verbose_name = 'Фото')
    category = models.ForeignKey(Categories , verbose_name = 'Категория', on_delete = models.CASCADE)



