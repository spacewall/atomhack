# Generated by Django 5.0.3 on 2024-03-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mars_client', '0002_rename_name_and_surname_report_author_report_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Название отчёта'),
        ),
    ]
