# Generated by Django 3.2.9 on 2021-11-28 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20211128_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='first_name',
            field=models.CharField(help_text='Ivan', max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='last_name',
            field=models.CharField(help_text='Ivanov', max_length=50, verbose_name='Фамилия'),
        ),
    ]