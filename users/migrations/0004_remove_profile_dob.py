# Generated by Django 5.0.3 on 2024-03-28 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_address_profile_age_profile_dob_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='dob',
        ),
    ]
