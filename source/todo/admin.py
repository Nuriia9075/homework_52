from django.contrib import admin

# Register your models here.
from todo.models import Task
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'end_date', 'status')
    list_filter = ('status',)
    search_fields = ('title',)
    fields = ['title','status', 'end_date', 'description']

admin.site.register(Task, TaskAdmin)