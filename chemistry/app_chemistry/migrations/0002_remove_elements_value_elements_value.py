# Generated by Django 4.1 on 2022-08-07 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_chemistry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elements',
            name='value',
        ),
        migrations.AddField(
            model_name='elements',
            name='value',
            field=models.ManyToManyField(to='app_chemistry.value', verbose_name='Wartościowość'),
        ),
    ]
