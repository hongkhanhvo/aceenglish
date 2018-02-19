# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-17 06:44
from __future__ import unicode_literals

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_apost_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, null=True, upload_to=main.models.get_image_path)),
                ('caption', models.CharField(max_length=4000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
