# Generated by Django 4.0.3 on 2022-04-21 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.IntegerField(max_length=20),
        ),
    ]
