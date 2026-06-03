from todo.views import task_add, tasks, task_detail, task_update
from django.urls import path

urlpatterns = [
    path("", tasks, name="tasks"),
    path("tasks/", tasks, name="tasks"),
    path("tasks/add/", task_add, name="task_add"),
    path("task/<int:pk>/", task_detail, name="task_detail"),
    path("task/<int:pk>/edit/", task_update, name="task_update"),
]