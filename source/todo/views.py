from django.shortcuts import render, redirect, get_object_or_404
from todo.forms import AddTodoForm
from todo.models.task import Task


# Create your views here.
def tasks(request):
    tasklist = Task.objects.all()
    return render(request, 'todolist/index.html', {'tasklist': tasklist})

def task_add(request):
    if request.method == 'POST':
       form = AddTodoForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = AddTodoForm()
    return render(request, 'todolist/task_add.html', {'form': form})

def task_detail(request, pk, *args,**kwargs):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    return render(request, 'todolist/task_detail.html', {'task': task})

def task_update(request, pk,  *args,**kwargs):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = AddTodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = AddTodoForm(instance=task)
    return render(request, 'todolist/task_update.html', {'form': form, 'task': task})
