# Generated by Django 4.0.5 on 2022-09-08 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
                ('send_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='contact_info',
        ),
    ]
