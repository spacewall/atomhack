from django.db import models


class Report(models.Model):
    name_and_surname = models.CharField(max_length=30, verbose_name='Фамилия, имя отправителя')
    context = models.TextField(verbose_name='Текст отчёта')
    release_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    send_date = models.DateTimeField(blank=True, verbose_name='Дата отправки')
    files = models.FileField(verbose_name='Дополнительные файлы', blank=True, null=True)


    class Meta:
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'
        ordering = ['release_date']

    
    def __str__(self) -> str:
        return self.name
