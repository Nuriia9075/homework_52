from account.urls import app_name
from todo.views.tasks import (
    TaskDeleteView,
    TaskUpdateView,
    TaskDetailView, ProjectTaskAddView,)
from todo.views.project import (ProjectListView, ProjectDetailView,
                                ProjectCreateView, ProjectDeleteView, ProjectUpdateView)
from django.urls import path


app_name = "todo"

urlpatterns = [
    path("", ProjectListView.as_view(), name="list"),
    path("projects/", ProjectListView.as_view(), name="projects"),
    path("project/<int:pk>/",ProjectDetailView.as_view(),  name="detail"),
    path("project/create/", ProjectCreateView.as_view(), name="create"),
    path("project/<int:pk>/delete/",ProjectDeleteView.as_view(), name="delete"),
    path("project/<int:pk>/detail/add/", ProjectTaskAddView.as_view(), name="task_add"),
    path("project/<int:pk>/detail/update/", ProjectUpdateView.as_view(), name="update"),

    path("task/<int:pk>/detail/",TaskDetailView.as_view(),  name="task_detail"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task_delete"),
]