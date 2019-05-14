# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-24 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyscada', '0034_auto_20170213_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceProtocol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('protocol', models.CharField(default='generic', max_length=400)),
                ('description', models.TextField(default=b'', null=True, verbose_name='Description')),
                ('app_name', models.CharField(default='pyscada.PROTOCOL', max_length=400)),
                ('device_class', models.CharField(default='pyscada.PROTOCOL.device', max_length=400)),
                ('daq_daemon', models.BooleanField()),
                ('single_thread', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='device',
            name='device_type',
        ),
        migrations.AddField(
            model_name='device',
            name='protocol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pyscada.DeviceProtocol'),
        ),
    ]
