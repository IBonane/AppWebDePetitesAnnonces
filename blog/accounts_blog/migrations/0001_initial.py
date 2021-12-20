# Generated by Django 3.2.8 on 2021-10-30 10:45

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('firstname', models.CharField(max_length=50, verbose_name='Nom')),
                ('lastname', models.CharField(max_length=50, verbose_name='Prénom')),
                ('email', models.EmailField(blank=True, max_length=255, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=13, unique=True, verbose_name='Numéro de téléphone')),
                ('password', models.CharField(max_length=15, verbose_name='Mot de passe')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]