# Generated by Django 4.0.6 on 2022-07-14 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creativeworld', '0003_alter_contactadmin_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
    ]
