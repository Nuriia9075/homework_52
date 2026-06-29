from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from todo.models import Project

User = get_user_model()

class UserDeleteView(LoginRequiredMixin, View):
    def post(self, request,*args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        user = get_object_or_404(User, pk=self.kwargs['user_pk'])
        project.users.remove(user)
        return redirect('todo:detail', pk=self.kwargs['project_pk'])


class UserAddView(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        user = get_object_or_404(User, pk=self.kwargs['user_pk'])
        project.users.add(user)
        return redirect('todo:detail', pk=self.kwargs['project_pk'])
