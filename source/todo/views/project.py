from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db.models import Q
from todo.forms import SimpleSearchForm, ProjectForm
from todo.models.project import Project
from urllib.parse import urlencode


class ProjectListView(ListView):
    template_name = "project/index.html"
    model = Project
    context_object_name = "projects"
    ordering = ["-created_at"]
    queryset = Project.objects.all()
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
                Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_value:
            context['query'] = urlencode({"search": self.search_value})
            context['search_value'] = self.search_value
        return context

class ProjectDetailView(DetailView):
    template_name = "project/detail.html"
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SimpleSearchForm()
        context['tasks'] = self.object.tasks.exclude(is_deleted=True)
        return context

class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = "project/create.html"
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SimpleSearchForm()
        return context

    def get_success_url(self):
        return reverse("todo:detail", kwargs={"pk": self.object.pk})

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "project/update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SimpleSearchForm()
        return context

    def get_success_url(self):
        return reverse("todo:detail", kwargs={"pk": self.kwargs['pk']})

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "project/delete.html"
    model = Project
    success_url = reverse_lazy("todo:projects")