# Generated by Django 5.0.4 on 2024-04-23 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_paymentdata_paid_true'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdata',
            name='payment_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paymentdata',
            name='rent_data',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.rentdata'),
        ),
    ]
