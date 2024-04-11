# Generated by Django 5.0.4 on 2024-04-11 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclesforrent',
            name='color',
            field=models.CharField(blank=True, max_length=65),
        ),
        migrations.AddField(
            model_name='vehiclesforrent',
            name='engine_val',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='vehiclesforrent',
            name='logo',
            field=models.ImageField(null=True, upload_to='vehicles_logo'),
        ),
        migrations.AddField(
            model_name='vehiclesforrent',
            name='type',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='vehiclesforrent',
            name='year',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='vehiclesforrent',
            name='price',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
