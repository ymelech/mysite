# Generated by Django 2.1 on 2018-08-27 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0002_remove_device_typ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='repaired_at',
            field=models.DateTimeField(),
        ),
    ]
