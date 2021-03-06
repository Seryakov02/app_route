# Generated by Django 3.2 on 2021-05-12 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210502_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='image',
            field=models.ImageField(null=True, upload_to='buses/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='bus',
            name='number',
            field=models.IntegerField(verbose_name='Номер автобуса'),
        ),
        migrations.AlterField(
            model_name='bus',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='race',
            name='bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bus', verbose_name='Номер автобуса'),
        ),
        migrations.AlterField(
            model_name='race',
            name='first_point_of_departure',
            field=models.CharField(max_length=255, null=True, verbose_name='Первый пункт отправления'),
        ),
        migrations.AlterField(
            model_name='race',
            name='second_point_of_departure',
            field=models.CharField(max_length=255, null=True, verbose_name='Второй пункт отправления'),
        ),
        migrations.AlterField(
            model_name='race',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='url'),
        ),
    ]
