# Generated by Django 3.2 on 2021-05-16 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_race_route'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='bus_brand',
            field=models.CharField(default='', max_length=255, verbose_name='Марка автобуса'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bus',
            name='driver',
            field=models.CharField(default='', max_length=255, verbose_name='Имя водителя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bus',
            name='number_of_places',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Число мест'),
        ),
    ]
