# Generated by Django 3.0.8 on 2020-08-11 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edunet', '0009_auto_20200810_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='department_abbrievation',
            # field=models.CharField(default='Department Abbrievation', max_length=10),
            field=models.CharField(max_length=10),
        ),
    ]