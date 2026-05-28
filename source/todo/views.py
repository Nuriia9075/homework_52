from django.shortcuts import render, redirect
from todo.models import Task, status_task


# Create your views here.
def tasks(request):
    tasklist = Task.objects.all()
    return render(request, 'index.html', {'tasklist': tasklist})

def task_add(request):
    if request.method == 'POST':
        if not request.POST['end_date']:
            end_date_value = None
        else : end_date_value = request.POST['end_date']
        if not request.POST['description']:
            description_value = None
        else:
            description_value = request.POST['description']
        Task.objects.create(
        title = request.POST['title'],
        status = request.POST['status'],
        end_date = end_date_value,
        description = description_value,
        )
        return redirect('/tasks')
    return render(request, 'task_add.html', {'status_task': status_task})

def task_detail(request, task_id):
    if request.method == 'GET':
        try:
            task = Task.objects.get(id = int(task_id))
            return render(request, 'task_detail.html', {'task': task})
        except Task.DoesNotExist:
            return redirect('/tasks')
    else:
        task = Task.objects.get(id = int(task_id))
        task.delete()
        return redirect('/tasks')
