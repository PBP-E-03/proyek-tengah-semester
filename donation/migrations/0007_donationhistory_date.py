# Generated by Django 4.1.2 on 2022-12-12 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0006_alter_donationhistory_payment_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationhistory',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
