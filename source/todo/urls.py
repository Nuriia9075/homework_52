from todo.views import task_add, tasks, task_detail
from django.urls import path

urlpatterns = [
    path("", tasks, name="tasks"),
    path("tasks/", tasks, name="tasks"),
    path("tasks/add/", task_add, name="task_add"),
    path("task/<int:task_id>", task_detail, name="task_detail"),
]