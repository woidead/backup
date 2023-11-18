from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    des = models.TextField(verbose_name='заметки')
    create_ad = models.DateTimeField(auto_now_add=True)