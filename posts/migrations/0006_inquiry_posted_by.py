# Generated by Django 5.0.3 on 2024-04-06 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_inquiry_advertise'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='posted_by',
            field=models.CharField(default='vaibhav', max_length=100),
            preserve_default=False,
        ),
    ]
