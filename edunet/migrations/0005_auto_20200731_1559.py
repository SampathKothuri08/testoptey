# Generated by Django 3.0.8 on 2020-07-31 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edunet', '0004_tree_of_knowledge_transcript_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree_of_knowledge',
            name='transcript_num',
            field=models.IntegerField(),
        ),
    ]
