# Generated by Django 4.1.2 on 2022-10-29 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpfe', '0007_alter_signup_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='nom',
            new_name='name',
        ),
    ]
