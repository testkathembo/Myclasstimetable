# Generated by Django 5.1.1 on 2024-09-28 22:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faculties', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='admin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_admin', to='users.customuser'),
        ),
    ]
