# Generated by Django 4.2 on 2023-04-21 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0008_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentmodel',
            name='percentage',
        ),
    ]
