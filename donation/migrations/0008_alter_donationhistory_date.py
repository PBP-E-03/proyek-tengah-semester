# Generated by Django 4.1.2 on 2022-12-12 09:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0007_donationhistory_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationhistory',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 9, 58, 35, 123288, tzinfo=datetime.timezone.utc)),
        ),
    ]
