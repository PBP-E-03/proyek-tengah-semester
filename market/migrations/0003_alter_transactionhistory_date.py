# Generated by Django 4.1.2 on 2022-11-02 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_remove_product_image_url_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionhistory',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
