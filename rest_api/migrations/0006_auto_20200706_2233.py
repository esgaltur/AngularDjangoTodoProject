# Generated by Django 3.0.8 on 2020-07-06 20:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0005_auto_20200706_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='targetDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]