# Generated by Django 3.0.3 on 2020-03-24 22:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_auto_20200324_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogindexpage',
            name='banner',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='image',
        ),
    ]
