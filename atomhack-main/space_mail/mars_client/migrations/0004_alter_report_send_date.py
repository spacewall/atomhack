# Generated by Django 5.0.3 on 2024-03-08 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mars_client', '0003_alter_report_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='send_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата отправки'),
        ),
    ]
