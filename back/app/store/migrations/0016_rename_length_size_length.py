# Generated by Django 4.2.2 on 2023-09-12 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_characteristics_torque_alter_size_wheel_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='size',
            old_name='Length',
            new_name='length',
        ),
    ]
