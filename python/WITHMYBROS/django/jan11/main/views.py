from django.shortcuts import render
from main.models import Todo
from django.http import HttpResponseRedirect

# Create your views here.
def main(request):
    todo = Todo.objects.all()
    return render (request, 'index.html', {'todo':todo})
def saving(request):
    if request.method == 'POST':
        todo = Todo()
        todo.title = request.POST.get('name')
        todo.des = request.POST.get('text')
        todo.save()
    return HttpResponseRedirect('/')