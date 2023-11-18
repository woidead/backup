from django.db import models

# Create your models here.

class Brand(models.Model):
    title = models.CharField(max_length = 50, verbose_name = 'brand')
    def __str__(self):
        return self.title


class Cross(models.Model):
    name = models.CharField(max_length = 20, verbose_name = 'кроссовок' )
    image = models.ImageField(upload_to = 'main', verbose_name = 'фото')
    desc = models.TextField( verbose_name = 'описание')
    category = models.ForeignKey(Brand, verbose_name = 'Брeнд', on_delete = models.CASCADE )