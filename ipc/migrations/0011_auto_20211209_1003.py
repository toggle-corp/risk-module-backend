# Generated by Django 3.2.8 on 2021-12-09 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipc', '0010_thinkhazardcountry_thinkhazardinformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globaldisplacement',
            name='hazard_type',
            field=models.CharField(blank=True, choices=[('EQ', 'Earthquake'), ('FL', 'Flood'), ('TC', 'Cyclone'), ('EP', 'Epidemic'), ('FI', 'Food Insecurity'), ('SS', 'Storm Surge'), ('DR', 'Drought'), ('TS', 'Tsunami'), ('CD', 'Cyclonic Wind')], max_length=100, verbose_name='hazard type'),
        ),
        migrations.AlterField(
            model_name='ipc',
            name='hazard_type',
            field=models.CharField(blank=True, choices=[('EQ', 'Earthquake'), ('FL', 'Flood'), ('TC', 'Cyclone'), ('EP', 'Epidemic'), ('FI', 'Food Insecurity'), ('SS', 'Storm Surge'), ('DR', 'Drought'), ('TS', 'Tsunami'), ('CD', 'Cyclonic Wind')], max_length=100, verbose_name='hazard type'),
        ),
        migrations.AlterField(
            model_name='ipcmonthly',
            name='hazard_type',
            field=models.CharField(blank=True, choices=[('EQ', 'Earthquake'), ('FL', 'Flood'), ('TC', 'Cyclone'), ('EP', 'Epidemic'), ('FI', 'Food Insecurity'), ('SS', 'Storm Surge'), ('DR', 'Drought'), ('TS', 'Tsunami'), ('CD', 'Cyclonic Wind')], max_length=100, verbose_name='hazard type'),
        ),
        migrations.AlterField(
            model_name='thinkhazardinformation',
            name='hazard_type',
            field=models.CharField(blank=True, choices=[('EQ', 'Earthquake'), ('FL', 'Flood'), ('TC', 'Cyclone'), ('EP', 'Epidemic'), ('FI', 'Food Insecurity'), ('SS', 'Storm Surge'), ('DR', 'Drought'), ('TS', 'Tsunami'), ('CD', 'Cyclonic Wind')], max_length=100, verbose_name='hazard type'),
        ),
    ]
