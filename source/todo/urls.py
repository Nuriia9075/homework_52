from todo.views.tasks import (
    TaskAddView,
    TaskListView,
    TaskDeleteView,
    TaskUpdateView,
    TaskDetailView)
from todo.views.project import (ProjectListView, ProjectDetailView, ProjectCreateView)

from django.urls import path

urlpatterns = [
    path("", ProjectListView.as_view(), name="list"),
    path("projects/", ProjectListView.as_view(), name="projects"),
    path("project/<int:pk>/",ProjectDetailView.as_view(),  name="detail"),
    path("project/create/", ProjectCreateView.as_view(), name="create"),

    path("tasks/", TaskListView.as_view(), name="tasks"),
    path("tasks/add/", TaskAddView.as_view(), name="task_add"),
    path("task/<int:pk>/",TaskDetailView.as_view(),  name="task_detail"),
    path("task/<int:pk>/edit/", TaskUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
]