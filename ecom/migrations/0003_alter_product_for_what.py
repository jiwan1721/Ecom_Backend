# Generated by Django 4.0.4 on 2022-11-26 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_contactus_contact_number_contactus_deascriptions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='for_what',
            field=models.CharField(choices=[('Hotel', 'Hotel'), ('School', 'School'), ('Other', 'Other'), ('Park', 'Park'), ('Resturant', 'Resturant')], default='Other', max_length=100),
        ),
    ]
