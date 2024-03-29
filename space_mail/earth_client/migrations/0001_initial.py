# Generated by Django 5.0.3 on 2024-03-10 10:36

import django_ckeditor_5.fields
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
                ('name', models.CharField(max_length=40, verbose_name='Название отчёта')),
                ('author', models.CharField(max_length=30, verbose_name='Фамилия, имя отправителя')),
                ('context', django_ckeditor_5.fields.CKEditor5Field(blank=True, verbose_name='Текст отчёта')),
                ('release_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('send_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата отправки')),
                ('files', models.FileField(blank=True, null=True, upload_to='', verbose_name='Дополнительные файлы')),
            ],
            options={
                'verbose_name': 'Отчёт',
                'verbose_name_plural': 'Отчёты',
                'ordering': ['release_date'],
            },
        ),
    ]
