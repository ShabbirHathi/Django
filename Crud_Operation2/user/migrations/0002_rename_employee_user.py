# Generated by Django 4.0.3 on 2022-04-20 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='User',
        ),
    ]
