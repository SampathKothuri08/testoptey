# Generated by Django 3.0.8 on 2020-07-30 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edunet', '0002_course_course_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_description',
            field=models.TextField(max_length=1000),
        ),
        migrations.CreateModel(
            name='Tree_of_Knowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tree_of_knowledge', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edunet.Course')),
            ],
        ),
    ]
