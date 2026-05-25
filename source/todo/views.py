from django.shortcuts import render
from todo.models import Task


# Create your views here.
def tasks(request):
    tasklist = Task.objects.all()
    return render(request, 'index.html', {'tasklist': tasklist})

def task_add(request):
    if request.method == 'POST':
        pass

def task_detail(request, id):
    pass