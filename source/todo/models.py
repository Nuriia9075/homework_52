from django.db import models

# Create your models here.
status_task =[('new','новое'), ('in_progress','в процессе'), ('done', 'сделано')]
class Task(models.Model):
    title = models.CharField(max_length=100,verbose_name= "Название")
    status = models.CharField(max_length= 50, choices=status_task, default='new')
    end_date = models.DateField(null=True, verbose_name="Дата завершения")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task'
        verbose_name = 'Задача'