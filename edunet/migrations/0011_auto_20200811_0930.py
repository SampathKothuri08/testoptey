# Generated by Django 3.0.8 on 2020-08-11 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edunet', '0010_department_department_abbrievation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='department_abbrievation',
            new_name='department_abbreviation',
        ),
    ]
