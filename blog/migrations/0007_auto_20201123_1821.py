# Generated by Django 2.2.3 on 2020-11-23 10:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201120_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='modified_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified_time'),
        ),
    ]