# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-17 09:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_galleryphotos'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, null=True, upload_to='hinh-anh-lop-hoc/')),
                ('caption', models.CharField(max_length=4000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, null=True, upload_to=main.models.get_image_path)),
                ('content', models.CharField(max_length=4000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='main.Category')),
            ],
        ),
        migrations.RemoveField(
            model_name='apost',
            name='category',
        ),
        migrations.DeleteModel(
            name='GalleryPhotos',
        ),
        migrations.DeleteModel(
            name='aPost',
        ),
    ]