# Generated by Django 2.2.5 on 2020-06-09 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_company_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='company',
        ),
    ]
