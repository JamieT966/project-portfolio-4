# Generated by Django 3.2.14 on 2022-07-21 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='selected_time',
            field=models.TimeField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='booking',
            name='selected_date',
            field=models.DateField(blank=True, null=True, verbose_name='Selected Date: mm/dd/yyyy'),
        ),
    ]
