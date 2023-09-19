# Generated by Django 4.0.6 on 2023-09-16 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DowellGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('meter', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
