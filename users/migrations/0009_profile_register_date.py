# Generated by Django 5.0.3 on 2024-03-30 23:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_profile_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='register_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
