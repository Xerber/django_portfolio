# Generated by Django 4.0.5 on 2022-06-20 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_socialcontact_remove_myinfo_class_facebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialcontact',
            name='boot_class',
            field=models.CharField(default='fa fa-', max_length=100, verbose_name='Bootstrap класс иконки'),
        ),
        migrations.AlterField(
            model_name='socialcontact',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название в админке'),
        ),
    ]