# Generated by Django 3.2.9 on 2021-11-28 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='first_name',
            field=models.CharField(help_text='Иван', max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='last_name',
            field=models.CharField(help_text='Иванов', max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='make',
            field=models.CharField(blank=True, help_text='Opel', max_length=30, verbose_name='Автоконцерн'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(blank=True, help_text='Corsa D', max_length=30, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='plate_number',
            field=models.CharField(blank=True, help_text='AA 1234 OO', max_length=30, unique=True, verbose_name='Номерной знак'),
        ),
    ]
