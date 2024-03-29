# Generated by Django 4.0.6 on 2023-05-11 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('portfolio', models.CharField(max_length=300)),
                ('productName', models.CharField(max_length=300)),
                ('action', models.BooleanField(default=True)),
                ('orgName', models.CharField(max_length=300)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('image_url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FavouriteImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=300)),
                ('username', models.CharField(max_length=300)),
                ('image', models.TextField()),
            ],
        ),
    ]
