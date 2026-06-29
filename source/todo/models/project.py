from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField( max_length=200,verbose_name= "Название")
    description = models.TextField(null=True, verbose_name='Описание', blank=True)
    created_at = models.DateField(verbose_name="Дата создания")
    end_at = models.DateField( null = True, blank=True ,verbose_name ="Дата окончания")
    users = models.ManyToManyField(User, related_name='projects', verbose_name="Участники проекта")
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'project'
        verbose_name = 'Проект'