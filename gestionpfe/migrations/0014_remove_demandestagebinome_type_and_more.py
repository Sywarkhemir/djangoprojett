# Generated by Django 4.1.2 on 2022-11-18 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpfe', '0013_demandestagebinome_type_demandestagemonome_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demandestagebinome',
            name='type',
        ),
        migrations.RemoveField(
            model_name='demandestagemonome',
            name='type',
        ),
    ]
