# Generated by Django 4.1 on 2022-08-25 14:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile', verbose_name='image')),
                ('addres', models.CharField(max_length=50, verbose_name='address')),
                ('join_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='created at')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='slug')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
