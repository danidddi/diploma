# Generated by Django 4.2.2 on 2023-07-04 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_car_images_alter_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='images',
            new_name='image',
        ),
    ]
