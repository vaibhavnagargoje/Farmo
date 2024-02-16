# Generated by Django 4.2.7 on 2024-02-16 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_seller_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactName', models.CharField(max_length=100)),
                ('contactMail', models.CharField(max_length=100)),
                ('contactPhone', models.CharField(max_length=15)),
                ('contactMessage', models.CharField(max_length=500)),
            ],
        ),
    ]
