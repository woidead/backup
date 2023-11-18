from asyncio import queues
from django.shortcuts import render
from main.serializers import CrossSerilazer
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView 
from main.models import *
# Create your views here.

class AboutCross(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = CrossSerilazer
    cross = Cross.objects.all()

    def get_queryset(self):
        queryset = Cross.objects.all()
        return queryset        
    def get(self, requst):
        return self.list(requst)
    
    def post(self, request, format = None):
        return self.create(request)

