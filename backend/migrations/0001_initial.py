# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 20:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capacity',
            fields=[
                ('cap_id', models.AutoField(primary_key=True, serialize=False)),
                ('cap_name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'capacity',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.IntegerField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=10)),
                ('area_name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('ins_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ins_type', models.CharField(max_length=10)),
                ('ins_name', models.CharField(max_length=51)),
                ('agent', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='backend.City')),
            ],
            options={
                'db_table': 'institution',
            },
        ),
        migrations.CreateModel(
            name='Institutions_Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_bed', models.CharField(max_length=20)),
                ('Ins_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institution', to='backend.Institution')),
                ('cap_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='capacity', to='backend.Capacity')),
            ],
            options={
                'db_table': 'institution_unit',
            },
        ),
        migrations.AlterUniqueTogether(
            name='institutions_unit',
            unique_together=set([('Ins_id', 'cap_id')]),
        ),
    ]