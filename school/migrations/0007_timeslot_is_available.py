# Generated by Django 5.1.4 on 2025-01-23 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_classtimetable_delete_timetable'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
