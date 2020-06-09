# Generated by Django 2.2.5 on 2020-06-09 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0003_remove_event_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='planner.Category'),
        ),
        migrations.AlterField(
            model_name='event',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='due_date',
            field=models.DateTimeField(),
        ),
    ]
