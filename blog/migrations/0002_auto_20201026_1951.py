# Generated by Django 2.2.3 on 2020-10-26 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='odified_time',
            new_name='created_time',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='reated_time',
            new_name='modified_time',
        ),
    ]
