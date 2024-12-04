# Generated by Django 3.0 on 2024-05-02 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edunet', '0018_auto_20200825_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='PuzzleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='puzzle_images/')),
                ('title', models.CharField(default='', max_length=255)),
                ('puzzle_of_knowledge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edunet.PuzzleOfKnowledge')),
            ],
        ),
    ]