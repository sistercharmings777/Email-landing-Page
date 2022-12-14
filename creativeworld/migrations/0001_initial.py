# Generated by Django 4.0.6 on 2022-07-14 15:28

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
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('subject', models.CharField(max_length=400, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='ContactAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=10, verbose_name='Contact')),
                ('location', models.CharField(max_length=200, verbose_name='Location')),
                ('twitter', models.URLField(verbose_name='Twitter')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('instagram', models.URLField(verbose_name='Instagram')),
                ('linkedin', models.URLField(verbose_name='LinkedIn')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
