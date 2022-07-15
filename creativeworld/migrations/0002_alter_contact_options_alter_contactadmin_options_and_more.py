# Generated by Django 4.0.6 on 2022-07-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creativeworld', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='contactadmin',
            options={'verbose_name': 'Contact Administration', 'verbose_name_plural': 'Contact Administration'},
        ),
        migrations.AddField(
            model_name='contactadmin',
            name='address',
            field=models.CharField(default='', max_length=200, verbose_name='Address'),
        ),
    ]
