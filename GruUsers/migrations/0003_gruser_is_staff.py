# Generated by Django 2.0 on 2018-03-23 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GruUsers', '0002_remove_gruser_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='gruser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
