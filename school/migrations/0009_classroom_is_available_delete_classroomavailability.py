# Generated by Django 5.1.4 on 2025-01-24 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_alter_classroomavailability_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='ClassroomAvailability',
        ),
    ]
