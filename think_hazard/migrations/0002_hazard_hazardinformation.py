# Generated by Django 3.2.7 on 2021-09-21 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('think_hazard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HazardInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hazard_level', models.CharField(blank=True, choices=[(' LOW', 'Low'), ('VLO', 'Very Low'), ('MED', 'Medium'), ('HIG', 'High'), ('no-data', 'No Data')], max_length=10, verbose_name='hazard level')),
                ('hazard_type', models.CharField(blank=True, choices=[('EQ', 'Earthquake'), ('TS', 'Tsunami'), ('VO', 'Volcano'), ('CY', 'Cyclones'), ('FL', 'Floods'), ('UF', 'Urban Floods'), ('CF', 'Coastal Floods'), ('LS', 'Landslides'), ('EH', 'Extreme Heat'), ('WF', 'WildFires'), ('DR', 'Drought')], max_length=20, verbose_name='hazard type')),
            ],
        ),
        migrations.CreateModel(
            name='Hazard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='think_hazard.thinkhazardcountry')),
                ('hazard_informations', models.ManyToManyField(blank=True, to='think_hazard.HazardInformation')),
            ],
        ),
    ]
