# Generated by Django 4.0.6 on 2023-07-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Announcement', '0002_alter_announcement_member_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='company_id',
            new_name='org_id',
        ),
        migrations.AddField(
            model_name='announcement',
            name='org_name',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='announcement',
            name='title',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]
