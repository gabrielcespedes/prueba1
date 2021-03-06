# Generated by Django 2.2 on 2021-05-24 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('ram', models.IntegerField()),
                ('almacenamiento', models.IntegerField()),
                ('tamaño_pantalla', models.FloatField()),
                ('fabricante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phone.Fabricante')),
            ],
        ),
    ]
