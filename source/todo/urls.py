from todo.views import (
    TaskAddView,
    TaskListView,
    TaskDeleteView,
    TaskUpdateView,
    TaskDetailView)

from django.urls import path

urlpatterns = [
    path("", TaskListView.as_view(), name="list"),
    path("tasks/", TaskListView.as_view(), name="tasks"),
    path("tasks/add/", TaskAddView.as_view(), name="task_add"),
    path("task/<int:pk>/",TaskDetailView.as_view(),  name="task_detail"),
    path("task/<int:pk>/edit/", TaskUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
]