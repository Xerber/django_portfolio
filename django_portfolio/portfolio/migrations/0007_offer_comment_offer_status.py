# Generated by Django 4.0.5 on 2022-06-14 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_alter_offer_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='comment',
            field=models.TextField(max_length=5000, null=True, verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='offer',
            name='status',
            field=models.CharField(choices=[('Новая', 'Новая'), ('В работе', 'В работе'), ('Закрыта', 'Закрыта')], default='Новая', max_length=10, verbose_name='Месяц начала работы'),
        ),
    ]