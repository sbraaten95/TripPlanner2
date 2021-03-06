# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('buddy', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Companion', to='login.User')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('planner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='planner', to='login.User')),
            ],
        ),
        migrations.AddField(
            model_name='companion',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Companion', to='trips.Trip'),
        ),
    ]
