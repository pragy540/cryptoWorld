# Generated by Django 4.0.1 on 2022-01-12 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange_app', '0002_userapi_delete_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapi',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
