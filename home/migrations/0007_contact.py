# Generated by Django 4.2.7 on 2024-02-16 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_contact_delete_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Mail', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=15)),
                ('Message', models.CharField(max_length=500)),
            ],
        ),
    ]
