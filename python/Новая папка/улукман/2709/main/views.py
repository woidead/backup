from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from main.models import Categories, Meals  
# Create your views here.
def main(request):
    meal = Meals.objects.all()
    category= Categories.objects.all
    context = {'meal':meal, 'category': category}

    return render(request, 'index.html', context = context)

     

