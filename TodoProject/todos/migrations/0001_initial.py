# Generated by Django 3.0.3 on 2020-03-01 19:30

# Name: Tommy Cao
# Original Date: 11/04/16
# Updated: 3/3/20
# Description: Django Todo Create Read Update Delete (CRUD) with PostgreSQL.
# Using 'pipenv' for virtual environment.

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(max_length=50)),
            ],
        ),        
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.Priority')),
            ],
        ),
    ]
