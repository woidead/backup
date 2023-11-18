from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
# Create your views here.


def main(request):
    return HttpResponse('<h1>page womens app</h1>')


def categories(request, catid):
    if (request.GET):
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1> <p> {catid}</p>")


def dog(request, doggy):

    return HttpResponse(f"Doggy:{doggy}")


def archive(request, year):
    if int(year) > 2020:
        # raise Http404() #возвращение ошибки 404
        return redirect('home', permanent=True) # перенаправление по клду 301 постаянное перенапраление
        # return redirect('/app') # перенаправление 301 временное

    return HttpResponse(f"<h1> Archive</h1> <p>{year}, архив этого года</p>")

def PageNotFound(request, exception):
    return HttpResponseNotFound('страница не найдена')