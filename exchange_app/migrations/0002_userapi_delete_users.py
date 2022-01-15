# Generated by Django 4.0.1 on 2022-01-12 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exchange_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserApi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wazirApi', models.CharField(blank=True, max_length=300)),
                ('wazirSecret', models.CharField(blank=True, max_length=300)),
                ('binanceApi', models.CharField(blank=True, max_length=300)),
                ('binanceSecret', models.CharField(blank=True, max_length=300)),
                ('ftxApi', models.CharField(blank=True, max_length=300)),
                ('ftxSecret', models.CharField(blank=True, max_length=300)),
                ('uniswapApi', models.CharField(blank=True, max_length=300)),
                ('uniswapSecret', models.CharField(blank=True, max_length=300)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]