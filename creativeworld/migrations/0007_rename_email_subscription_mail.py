# Generated by Django 4.0.6 on 2022-07-14 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creativeworld', '0006_alter_contact_email_alter_contact_message_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='email',
            new_name='mail',
        ),
    ]