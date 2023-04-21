# Generated by Django 4.2 on 2023-04-21 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('studentapp', '0010_delete_studentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('dateofbirth', models.DateField()),
                ('physics', models.IntegerField()),
                ('chemistry', models.IntegerField()),
                ('maths', models.IntegerField()),
                ('computerscience', models.IntegerField()),
                ('percentage', models.FloatField()),
            ],
        ),
    ]
