# Generated by Django 4.2.2 on 2023-07-19 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_images_car_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='store.car', verbose_name='Автомобиль'),
        ),
    ]
