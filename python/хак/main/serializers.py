from rest_framework import serializers
from main.models import *

class CrossSerilazer(serializers.ModelSerializer):
    class Meta:
        model = Cross
        fields = ['id', 'name', 'desc', 'image', 'category']