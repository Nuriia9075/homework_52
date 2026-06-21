from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View, ListView
from django.db.models import Q
from todo.forms import AddTodoForm, SimpleSearchForm
from todo.models.task import Task
from urllib.parse import urlencode


# Create your views here.
class TaskListView(ListView):
    template_name = "todolist/index.html"
    model = Task
    context_object_name = "tasks"
    ordering = ["-created_at"]
    queryset = Task.objects.all()
    paginate_by = 5
    paginate_orphans = 1

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(title__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_value:
            context['query'] = urlencode({"search": self.search_value})
            context['search_value'] = self.search_value
        return context

class TaskAddView(View):
    def get(self, request, *args, **kwargs):
        form = AddTodoForm()
        return render(request, 'todolist/task_add.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AddTodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        return render(request, 'todolist/task_add.html', {'form': form})


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
        form = AddTodoForm(instance=self.task)
        return render(request, 'todolist/task_update.html', {'form': form, 'task': self.task})

    def post(self, request, *args, **kwargs):
        form = AddTodoForm(request.POST, instance=self.task)
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