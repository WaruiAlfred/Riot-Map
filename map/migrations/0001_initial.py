# Generated by Django 3.2.8 on 2021-10-26 07:25

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Riot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('time_riot_started', models.TimeField()),
                ('riot_status', models.CharField(max_length=40)),
                ('nature_of_riot', models.CharField(max_length=40)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=30)),
                ('important_areas', models.TextField()),
                ('profile_pic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
