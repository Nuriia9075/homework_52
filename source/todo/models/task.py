from django.db import models
from todo.validators import validate_title


# Create your models here.
class Task(models.Model):
    title = models.CharField(validators= [validate_title], max_length=200,verbose_name= "Название")
    description = models.TextField(null=True, verbose_name='Подробное описание', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редактирование")
    status =models.ForeignKey('todo.Status', on_delete=models.PROTECT, related_name='tasks')
    type = models.ManyToManyField('todo.Type', related_name='tasks', verbose_name="Типы")
    project =models.ForeignKey('todo.Project', on_delete=models.CASCADE, related_name='tasks')
    is_deleted= models.BooleanField(default=False)
    class Meta:
        db_table = 'task'

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task'
        verbose_name = 'Задача'