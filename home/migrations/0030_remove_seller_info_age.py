# Generated by Django 4.2.7 on 2024-03-11 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_seller_info_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller_info',
            name='age',
        ),
    ]