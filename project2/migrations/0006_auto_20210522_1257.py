# Generated by Django 3.2.3 on 2021-05-22 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project2', '0005_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Tabel Brand'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Type Pakaian'},
        ),
        migrations.AlterModelTable(
            name='brand',
            table=None,
        ),
        migrations.AlterModelTable(
            name='type',
            table=None,
        ),
    ]