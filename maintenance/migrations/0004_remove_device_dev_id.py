# Generated by Django 2.1 on 2018-08-27 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0003_auto_20180827_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='dev_id',
        ),
    ]
