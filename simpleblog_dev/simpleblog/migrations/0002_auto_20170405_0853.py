# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simpleblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='name')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='simpleblog.PostCategory', verbose_name='category'),
        ),
    ]
