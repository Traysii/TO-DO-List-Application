# Generated by Django 4.2.4 on 2023-08-17 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]