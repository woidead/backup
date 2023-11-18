from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Women
from .serializers import WomenSerializer
# Create your views here.
# class WomenView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


class WomenView(APIView):
    def get(self, request):
        lst = Women.objects.all().values()
        return Response({"posts":list(lst)})

    def post(self, request):
        post_new = Women.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            category_id = request.data['category_id']
        )
        return Response({"post":model_to_dict(post_new)})

