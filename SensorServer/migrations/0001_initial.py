# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 06:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicationTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication', models.TextField(max_length=100, null=True)),
                ('heart_rate', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Walking',
            fields=[
                ('time', models.DateTimeField(primary_key=True, serialize=False, verbose_name='time')),
                ('heart_rate', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='medicationtable',
            name='time',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SensorServer.Walking'),
        ),
    ]
