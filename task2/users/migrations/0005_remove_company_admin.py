# Generated by Django 2.2.5 on 2020-06-09 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200609_0919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='admin',
        ),
    ]
