# Generated by Django 5.0.4 on 2024-04-19 16:27

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentdata',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='PaymentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('card_number', models.IntegerField(blank=True, null=True)),
                ('expry_date', models.IntegerField(blank=True, null=True)),
                ('cvv_cvc', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('rent_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.rentdata')),
            ],
        ),
    ]
