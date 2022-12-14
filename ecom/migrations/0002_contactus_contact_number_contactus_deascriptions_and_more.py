# Generated by Django 4.0.4 on 2022-11-26 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='contact_number',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='deascriptions',
            field=models.TextField(default=23),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.EmailField(default=23, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='Description',
            field=models.TextField(default=23),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.IntegerField(default=23),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='for_what',
            field=models.CharField(choices=[('Park', 'Park'), ('Resturant', 'Resturant'), ('School', 'School'), ('Hotel', 'Hotel'), ('Other', 'Other')], default='Other', max_length=100),
        ),
    ]
