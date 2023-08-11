# Generated by Django 4.0.6 on 2023-05-11 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.CharField(max_length=255)),
                ('created_by', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('member_type', models.CharField(max_length=255)),
                ('company_id', models.CharField(max_length=255)),
                ('created_at_position', models.CharField(max_length=255)),
            ],
        ),
    ]
