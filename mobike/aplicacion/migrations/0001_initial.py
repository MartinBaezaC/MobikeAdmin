# Generated by Django 2.1.2 on 2018-11-22 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=30)),
                ('apellido_usuario', models.CharField(max_length=30)),
                ('rut_usuario', models.CharField(max_length=30)),
                ('comuna_usuaro', models.CharField(max_length=30)),
                ('lugar_trabajo', models.CharField(max_length=30)),
            ],
        ),
    ]
