# Generated by Django 5.1.4 on 2025-01-27 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_classtimetable_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classtimetable',
            name='duration',
            field=models.CharField(default='2 hour', max_length=100),
        ),
    ]
