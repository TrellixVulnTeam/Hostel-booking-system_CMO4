# Generated by Django 2.1.7 on 2019-02-25 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostelbookingapp', '0013_hostel_room'),
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
