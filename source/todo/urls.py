from todo.views import task_add, tasks, task_detail
from django.urls import path

urlpatterns = [
    path("", tasks),
    path("tasks/", tasks),
    path("tasks/add/", task_add),
    path("task/<int>", task_detail),
]