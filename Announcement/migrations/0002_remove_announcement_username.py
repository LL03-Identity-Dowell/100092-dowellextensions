# Generated by Django 4.0.6 on 2023-05-08 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Announcement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='username',
        ),
    ]
