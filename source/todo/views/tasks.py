from django.views.generic import TemplateView, View
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db.models import Q
from todo.forms import SimpleSearchForm,TaskForm
from todo.models.project import Project
from  todo.models.task import Task
from urllib.parse import urlencode
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
class TaskListView(TemplateView):
    template_name = 'todolist/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all().order_by('-created_at')
        return context

class ProjectTaskAddView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todolist/task_add.html"

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        task = form.save(commit=False)
        task.project = project
        task.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("detail", kwargs={"pk": self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SimpleSearchForm()
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