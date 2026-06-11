from django.db import models


class Status(models.Model):
    title = models.CharField(max_length=200,verbose_name= "Название")
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'status'
        verbose_name = 'Статус'



class Type(models.Model):
    title = models.CharField(max_length=200,verbose_name= "Название")
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'type'
        verbose_name = 'Тип'