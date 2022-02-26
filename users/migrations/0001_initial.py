# Generated by Django 4.0.2 on 2022-02-26 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Username')),
                ('date_birth', models.DateField(default='2001-01-01', verbose_name='Date of Birth')),
                ('is_active', models.BooleanField(default=True, verbose_name='Status active')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Status admin')),
                ('slug', models.SlugField(unique=True, verbose_name='URL-address')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
