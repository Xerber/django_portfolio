# Generated by Django 4.0.5 on 2022-06-20 21:56

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_alter_socialcontact_boot_class_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myinfo',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='myinfo',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Телефон'),
        ),
    ]