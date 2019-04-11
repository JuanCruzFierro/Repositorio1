# Generated by Django 2.0.6 on 2019-04-09 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=254)),
                ('titulo', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaDevolucion', models.DateField(blank=True, null=True)),
                ('fechaPrestamo', models.DateField()),
                ('libroId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libroId', to='libreria.Libro')),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('apellido', models.CharField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='prestamo',
            name='socioId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socioId', to='libreria.Socio'),
        ),
    ]