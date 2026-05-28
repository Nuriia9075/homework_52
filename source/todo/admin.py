from django.contrib import admin

# Register your models here.
from todo.models import Task
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'end_date', 'status')
    list_filter = ('status',)
    search_fields = ('title',)
    fields = ['title','status', 'end_date', 'description']

admin.site.register(Task, TaskAdmin)


# <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
#         integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI"
#         crossorigin="anonymous"></script>