# Generated by Django 3.1.4 on 2020-12-10 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_auto_20201210_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='engine_volume',
            field=models.CharField(max_length=7),
        ),
    ]