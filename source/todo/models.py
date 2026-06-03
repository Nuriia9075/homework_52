from django.db import models

# Create your models here.
status_task =[('new','новая'), ('in_progress','в процессе'), ('done', 'сделано')]
class Task(models.Model):
    title = models.CharField(max_length=200,verbose_name= "Название")
    status = models.CharField(max_length= 50, choices=status_task, default='new', verbose_name='Статус')
    end_date = models.DateField(null=True, verbose_name="Дата завершения", blank=True)
    description = models.TextField(null=True, verbose_name='Подробное описание', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task'
        verbose_name = 'Задача'