# Generated by Django 4.2.1 on 2023-06-18 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suppliar_check',
            old_name='addres',
            new_name='address',
        ),
    ]