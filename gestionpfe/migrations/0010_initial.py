# Generated by Django 4.1.2 on 2022-11-03 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestionpfe', '0009_delete_login_delete_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemandeStageMonome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('ncin', models.CharField(max_length=8)),
                ('parcours', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('userun', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DemandeStageBinome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('ncin', models.CharField(max_length=8)),
                ('parcours', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('nom2', models.CharField(max_length=255)),
                ('prenom2', models.CharField(max_length=255)),
                ('ncin2', models.CharField(max_length=8)),
                ('parcours2', models.CharField(max_length=255)),
                ('email2', models.EmailField(max_length=255)),
                ('binome1', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='binomeone', to=settings.AUTH_USER_MODEL)),
                ('binome2', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='binometwo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
