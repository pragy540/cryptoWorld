# Generated by Django 4.0.1 on 2022-01-16 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange_app', '0006_rename_uniswapapi_userapi_uniswapprivate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapi',
            name='email',
            field=models.CharField(max_length=300),
        ),
    ]
