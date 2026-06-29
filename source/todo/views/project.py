from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import  get_user_model
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db.models import Q
from todo.forms import SimpleSearchForm, ProjectForm
from todo.models.project import Project
from urllib.parse import urlencode
User = get_user_model()


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
        context['all_users'] = User.objects.exclude(projects=self.object)
        return context

class ProjectCreateView(PermissionRequiredMixin, CreateView):
    template_name = "project/create.html"
    form_class = ProjectForm
    permission_required = 'todo.change_project'

    def has_permission(self):
        return self.request.user.is_authenticated and self.request.user.groups.filter(name='Project Manager').exists()

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.users.add(self.request.user)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SimpleSearchForm()
        return context

    def get_success_url(self):
        return reverse("todo:detail", kwargs={"pk": self.object.pk})



class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "project/update.html"

    def has_permission(self):
        project = self.get_object()
        return (self.request.user.is_authenticated and
                self.request.user.groups.filter(name='Project Manager').exists() and
                project.users.filter(pk=self.request.user.pk).exists())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SimpleSearchForm()
        return context

    def get_success_url(self):
        return reverse("todo:detail", kwargs={"pk": self.kwargs['pk']})

class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = "project/delete.html"
    model = Project
    success_url = reverse_lazy("todo:projects")

    def has_permission(self):
        project = self.get_object()
        return (self.request.user.is_authenticated and
                self.request.user.groups.filter(name='Project Manager').exists() and
                project.users.filter(pk=self.request.user.pk).exists())