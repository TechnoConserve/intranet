# Generated by Django 3.0.7 on 2020-06-13 20:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='FolderStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='box.Folder')),
            ],
        ),
    ]
