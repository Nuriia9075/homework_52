from django.contrib import admin
from todo.models.task import Task
from todo.models.status_type import Status, Type
from todo.models.project import Project

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_filter = ('status', 'type')
    search_fields = ('title',)
    fields = ['title', 'description', 'status', 'type', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
class TaskTypeAdmin(admin.ModelAdmin):
    fields = ['title']
class TaskStatusAdmin(admin.ModelAdmin):
    fields = ['title']
class ProjectAdmin(admin.ModelAdmin):
    fields = ['name', 'description','created_at', 'end_at']

admin.site.register(Task, TaskAdmin)
admin.site.register(Status, TaskStatusAdmin)
admin.site.register(Type, TaskTypeAdmin)
admin.site.register(Project, ProjectAdmin)


