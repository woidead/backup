from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField('Listing', related_name='liked_by', blank=True)

class Listing(models.Model):
    TYPES = (
        ('Apartment', 'Квартира'),
        ('Room', 'Комната'),
        ('Dormitory', 'Квартирант'),
        ('Hotel', 'Гостиница'),
        ('Commercial', 'Коммерческая недвижимость'),
    )

    PUBLICATION_TYPES = (
        ('Sale', 'Продажа'),
        ('Rent', 'Аренда'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=TYPES)
    publication_type = models.CharField(max_length=10, choices=PUBLICATION_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location_city = models.CharField(max_length=255)
    location_district = models.CharField(max_length=255)
    location_street = models.CharField(max_length=255)
    likes = models.ManyToManyField(UserProfile, related_name='liked_listings', blank=True)
    views = models.IntegerField(default=0)
    num_rooms = models.IntegerField()
    area = models.DecimalField(max_digits=6, decimal_places=2)
    floor = models.IntegerField()
    total_floors = models.IntegerField()
    extras = models.TextField(blank=True)
    deposit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
