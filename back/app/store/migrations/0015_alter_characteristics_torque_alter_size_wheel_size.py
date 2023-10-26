# Generated by Django 4.2.2 on 2023-09-12 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_remove_characteristics_model_alter_boost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characteristics',
            name='torque',
            field=models.CharField(null=True, verbose_name='Крутящий момент'),
        ),
        migrations.AlterField(
            model_name='size',
            name='wheel_size',
            field=models.CharField(max_length=100, null=True, verbose_name='Размер колёс'),
        ),
    ]