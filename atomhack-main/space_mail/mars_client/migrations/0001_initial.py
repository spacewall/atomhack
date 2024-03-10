# Generated by Django 5.0.3 on 2024-03-08 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_and_surname', models.CharField(max_length=30, verbose_name='Фамилия, имя отправителя')),
                ('context', models.TextField(verbose_name='Текст отчёта')),
                ('release_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('send_date', models.DateTimeField(blank=True, verbose_name='Дата отправки')),
                ('files', models.FileField(blank=True, null=True, upload_to='', verbose_name='Дополнительные файлы')),
            ],
            options={
                'verbose_name': 'Отчёт',
                'verbose_name_plural': 'Отчёты',
                'ordering': ['release_date'],
            },
        ),
    ]