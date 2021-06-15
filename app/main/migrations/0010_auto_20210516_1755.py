# Generated by Django 3.2 on 2021-05-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210516_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='image',
            field=models.ImageField(default='', upload_to='buses/', verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bus',
            name='slug',
            field=models.SlugField(default='', unique=True, verbose_name='url'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='race',
            name='first_point_of_departure',
            field=models.CharField(default='', max_length=255, verbose_name='Первый пункт отправления'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='race',
            name='first_shedule',
            field=models.TextField(default='', verbose_name='Расписание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='race',
            name='route',
            field=models.TextField(default='', verbose_name='Маршрут следования'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='race',
            name='second_point_of_departure',
            field=models.CharField(default='', max_length=255, verbose_name='Второй пункт отправления'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='race',
            name='second_shedule',
            field=models.TextField(default='', verbose_name='Расписание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='race',
            name='slug',
            field=models.SlugField(default='', unique=True, verbose_name='url'),
            preserve_default=False,
        ),
    ]
