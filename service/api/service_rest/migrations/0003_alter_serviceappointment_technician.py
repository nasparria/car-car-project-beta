# Generated by Django 4.0.3 on 2022-08-03 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0002_serviceappointment_vip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceappointment',
            name='technician',
            field=models.SmallIntegerField(),
        ),
    ]