# Generated by Django 3.2.8 on 2021-11-30 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipc', '0008_auto_20211130_0835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='globaldisplacement',
            name='is_projected',
        ),
        migrations.RemoveField(
            model_name='ipcmonthly',
            name='is_projected',
        ),
        migrations.AddField(
            model_name='globaldisplacement',
            name='estimation_type',
            field=models.CharField(blank=True, choices=[('current', 'Current'), ('first_projection', 'First Projection'), ('second_projection', 'Second Projection')], max_length=100, verbose_name='estimation type'),
        ),
        migrations.AddField(
            model_name='ipcmonthly',
            name='estimation_type',
            field=models.CharField(blank=True, choices=[('current', 'Current'), ('first_projection', 'First Projection'), ('second_projection', 'Second Projection')], max_length=100, verbose_name='estimation type'),
        ),
    ]
