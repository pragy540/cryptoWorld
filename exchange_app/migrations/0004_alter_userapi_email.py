# Generated by Django 4.0.1 on 2022-01-12 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exchange_app', '0003_alter_userapi_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapi',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
