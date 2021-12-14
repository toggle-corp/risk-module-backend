# Generated by Django 3.2.9 on 2021-12-14 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ipc', '0011_auto_20211209_1003'),
        ('oddrin', '0015_auto_20211209_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pdc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hazard_id', models.CharField(max_length=255, verbose_name='hazard id')),
                ('hazard_name', models.CharField(max_length=255, verbose_name='hazard name')),
                ('hazard_type', models.CharField(blank=True, choices=[('EQ', 'Earthquake'), ('FL', 'Flood'), ('TC', 'Cyclone'), ('EP', 'Epidemic'), ('FI', 'Food Insecurity'), ('SS', 'Storm Surge'), ('DR', 'Drought'), ('TS', 'Tsunami'), ('CD', 'Cyclonic Wind')], max_length=100, verbose_name='hazard type')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='latitude')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='longitude')),
                ('uuid', models.UUIDField(blank=True, null=True, verbose_name='uuid')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='end_date')),
            ],
        ),
        migrations.CreateModel(
            name='PdcDisplacement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hazard_type', models.CharField(blank=True, choices=[('EQ', 'Earthquake'), ('FL', 'Flood'), ('TC', 'Cyclone'), ('EP', 'Epidemic'), ('FI', 'Food Insecurity'), ('SS', 'Storm Surge'), ('DR', 'Drought'), ('TS', 'Tsunami'), ('CD', 'Cyclonic Wind')], max_length=100, verbose_name='hazard type')),
                ('population_exposure', models.FloatField(blank=True, null=True, verbose_name='population exposure')),
                ('capital_exposure', models.FloatField(blank=True, null=True, verbose_name='capital exposure')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ipc.country', verbose_name='country')),
                ('pdc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oddrin.pdc', verbose_name='pdc')),
            ],
        ),
    ]
