# Generated by Django 4.1.2 on 2022-11-05 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpfe', '0010_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demandestagebinome',
            name='binome2',
        ),
    ]