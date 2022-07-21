# Generated by Django 3.2.14 on 2022-07-21 16:11

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_booking_time_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time_choice',
            field=models.CharField(choices=[('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00')], max_length=100),
        ),
    ]
