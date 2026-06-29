from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import get_user_model
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from todo.models import Project

User = get_user_model()

class UserDeleteView(PermissionRequiredMixin, View):
    def post(self, request,*args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        user = get_object_or_404(User, pk=self.kwargs['user_pk'])
        project.users.remove(user)
        return redirect('todo:detail', pk=self.kwargs['project_pk'])

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        user_groups = self.request.user.groups.all()
        is_manager = user_groups.filter(name='Project Manager').exists()
        is_team_lead = user_groups.filter(name='Team Lead').exists()
        is_member = project.users.filter(pk=self.request.user.pk).exists()
        return (is_manager or is_team_lead) and is_member

class UserAddView(PermissionRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        user = get_object_or_404(User, pk=self.kwargs['user_pk'])
        project.users.add(user)
        return redirect('todo:detail', pk=self.kwargs['project_pk'])
    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        user_groups = self.request.user.groups.all()
        is_manager = user_groups.filter(name='Project Manager').exists()
        is_team_lead = user_groups.filter(name='Team Lead').exists()
        is_member = project.users.filter(pk=self.request.user.pk).exists()
        return (is_manager or is_team_lead) and is_member


