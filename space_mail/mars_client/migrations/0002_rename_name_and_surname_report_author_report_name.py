# Generated by Django 5.0.3 on 2024-03-08 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mars_client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='name_and_surname',
            new_name='author',
        ),
        migrations.AddField(
            model_name='report',
            name='name',
            field=models.CharField(max_length=40, null=True, verbose_name='Название отчёта'),
        ),
    ]