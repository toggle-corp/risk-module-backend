# Generated by Django 3.2.7 on 2021-09-15 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Earthquake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.CharField(max_length=100, verbose_name='event id')),
                ('event_title', models.CharField(max_length=255, verbose_name='event title')),
                ('event_place', models.CharField(blank=True, max_length=255, null=True, verbose_name='event place')),
                ('event_date', models.DateTimeField(blank=True, null=True, verbose_name='event date')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='updated at')),
                ('latitude', models.FloatField(verbose_name='latitude')),
                ('longitude', models.FloatField(verbose_name='longitude')),
                ('depth', models.FloatField(verbose_name='depth')),
                ('magnitude', models.FloatField(verbose_name='magnitude')),
                ('magnitude_type', models.CharField(choices=[('2', '2'), ('4', '4'), ('fa', 'fa'), ('H', 'H'), ('lg', 'lg'), ('m', 'm'), ('ma', 'ma'), ('mb', 'mb'), ('MbLg', 'MbLg'), ('Mb_lg', 'Mb_lg'), ('mc', 'mc'), ('md', 'md'), ('mdl', 'mdl'), ('Me', 'Me'), ('mfa', 'mfa'), ('mh', 'mh'), ('Mi', 'Mi'), ('mint', 'mint'), ('ml', 'ml'), ('mlg', 'mlg'), ('mlr', 'mlr'), ('mlv', 'mlv'), ('Ms', 'Ms'), ('ms_20', 'ms_20'), ('Mt', 'Mt'), ('mun', 'mun'), ('mw', 'mw'), ('mwb', 'mwb'), ('mwc', 'mwc'), ('mwp', 'mwp'), ('mwr', 'mwr'), ('mwm', 'mwm'), ('no', 'no'), ('uk', 'uk'), ('Unknown', 'Unknown')], max_length=20, verbose_name='magnitude type')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='country')),
            ],
        ),
    ]
