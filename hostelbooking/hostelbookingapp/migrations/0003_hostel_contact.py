# Generated by Django 2.1.7 on 2019-02-22 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelbookingapp', '0002_hostel_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='contact',
            field=models.CharField(default='90909', max_length=10),
        ),
    ]
