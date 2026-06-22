from django.views.generic import TemplateView, View
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db.models import Q
from todo.models.project import Project
from django.shortcuts import render, redirect, get_object_or_404


from django.http import Http404
from django.views.generic import DetailView
from todo.models.task import Task
from todo.forms import SimpleSearchForm, TaskForm

class TaskDetailView(DetailView):
    model = Task
    template_name = "todolist/task_detail.html"
    context_object_name = "task"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.is_deleted:
            raise Http404("Задача не найдена или была удалена")
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SimpleSearchForm()
        return context

class ProjectTaskAddView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todolist/task_add.html"

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        task = form.save(commit=False)
        task.project = project
        task.is_deleted = False
        task.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("detail", kwargs={"pk": self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SimpleSearchForm()
        return context

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todolist/task_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SimpleSearchForm()
        return context

    def get_success_url(self):
        return reverse("detail", kwargs={"pk": self.object.project.pk})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todolist/task_confirm_delete.html"

    def form_valid(self, form):
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.save()
        return redirect('detail', pk=self.object.project.pk)
