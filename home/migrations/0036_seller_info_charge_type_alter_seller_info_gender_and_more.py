# Generated by Django 4.2.7 on 2024-03-12 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_seller_info_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller_info',
            name='charge_type',
            field=models.CharField(choices=[('Hour', 'Hr'), ('Day', 'Day'), ('Km', 'Km')], default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='seller_info',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='seller_info',
            name='product_catg',
            field=models.CharField(choices=[('Workers', 'Worker'), ('Machinerys', 'Machinery'), ('Vehicles', 'Vehicles')], max_length=10),
        ),
    ]