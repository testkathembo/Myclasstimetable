# Generated by Django 5.1 on 2024-10-11 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_faculty_alter_lecturer_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='school.faculty'),
        ),
    ]
