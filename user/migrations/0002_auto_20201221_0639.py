# Generated by Django 3.1.4 on 2020-12-21 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='favourite',
            new_name='favourite_car',
        ),
    ]
