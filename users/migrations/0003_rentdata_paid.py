# Generated by Django 5.0.4 on 2024-04-19 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rentdata_created_at_paymentdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentdata',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]