# Generated by Django 4.0.3 on 2022-11-25 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormularioCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=21, null=True, unique=True)),
                ('titulo', models.CharField(max_length=66)),
                ('descripcion', models.CharField(max_length=66)),
            ],
        ),
    ]
