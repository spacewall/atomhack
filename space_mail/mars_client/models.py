from django.db import models


class Report(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название отчёта')
    author = models.CharField(max_length=30, verbose_name='Фамилия, имя отправителя')
    context = models.TextField(verbose_name='Текст отчёта')
    release_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    send_date = models.DateTimeField(blank=True, verbose_name='Дата отправки', null=True)
    files = models.FileField(verbose_name='Дополнительные файлы', blank=True, null=True)


    class Meta:
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'
        ordering = ['release_date']

    
    def __str__(self) -> str:
        return self.name
