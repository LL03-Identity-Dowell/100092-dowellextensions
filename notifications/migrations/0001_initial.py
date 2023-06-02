# Generated by Django 4.0.6 on 2023-06-02 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.CharField(max_length=255)),
                ('org_id', models.CharField(max_length=255)),
                ('data_type', models.CharField(max_length=255)),
                ('user_type', models.CharField(max_length=255)),
                ('from_field', models.CharField(max_length=255)),
                ('to', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('org_name', models.CharField(max_length=255)),
                ('created_by', models.CharField(max_length=255)),
                ('meant_for', models.CharField(max_length=255)),
                ('flag', models.BooleanField()),
                ('type_of_notification', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('document_id', models.CharField(blank=True, max_length=300, null=True)),
                ('document_type', models.CharField(default='notification', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ProductNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_id', models.CharField(blank=True, max_length=300, null=True)),
                ('document_type', models.CharField(default='product_notification', max_length=300)),
                ('username', models.CharField(max_length=300)),
                ('portfolio', models.CharField(max_length=300)),
                ('product_name', models.CharField(max_length=300)),
                ('company_id', models.CharField(max_length=300, null=True)),
                ('org_name', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=500)),
                ('message', models.CharField(max_length=500)),
                ('link', models.CharField(blank=True, max_length=2048, null=True)),
                ('duration', models.CharField(max_length=300, null=True)),
                ('is_seen', models.BooleanField(default=False)),
                ('button_status', models.CharField(blank=True, max_length=300, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
