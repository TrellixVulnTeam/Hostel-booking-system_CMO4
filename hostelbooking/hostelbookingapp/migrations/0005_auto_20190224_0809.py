# Generated by Django 2.1.7 on 2019-02-24 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostelbookingapp', '0004_auto_20190223_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostel',
            name='city',
        ),
        migrations.RemoveField(
            model_name='room',
            name='hostel',
        ),
        migrations.DeleteModel(
            name='Hostel',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
