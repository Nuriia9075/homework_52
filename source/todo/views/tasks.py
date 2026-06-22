from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View
from todo.forms import TaskForm
from todo.models.task import Task


# Create your views here.
class TaskListView(TemplateView):
    template_name = 'todolist/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all().order_by('-created_at')
        return context

class TaskDetailView(TemplateView):
    template_name = 'todolist/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        return context


class TaskUpdateView(View):
    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = TaskForm(instance=self.task)
        return render(request, 'todolist/task_update.html', {'form': form, 'task': self.task})

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST, instance=self.task)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=self.task.pk)
        return render(request, 'todolist/task_update.html', {'form': form, 'task': self.task})


class TaskDeleteView(View):
    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.task.delete()
        return redirect('tasks')