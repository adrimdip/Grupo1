# Generated by Django 4.2.5 on 2023-09-14 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActoJuridico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Escribano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escribano', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['escribano'],
            },
        ),
        migrations.CreateModel(
            name='Escritura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de Escritura')),
                ('folio', models.SmallIntegerField(blank=True, null=True)),
                ('otorgante', models.CharField(max_length=300)),
                ('aceptante', models.CharField(max_length=300)),
                ('acto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='escribania.actojuridico', verbose_name='Acto Jurídico')),
                ('escribano', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='escribania.escribano')),
            ],
        ),
    ]
