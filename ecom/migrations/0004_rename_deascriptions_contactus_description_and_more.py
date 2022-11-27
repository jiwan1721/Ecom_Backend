# Generated by Django 4.1.3 on 2022-11-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0003_alter_product_for_what'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='deascriptions',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='companyowner',
            name='phone_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='for_what',
            field=models.CharField(choices=[('Other', 'Other'), ('School', 'School'), ('Park', 'Park'), ('Hotel', 'Hotel'), ('Resturant', 'Resturant')], default='Other', max_length=100),
        ),
    ]
