# Generated by Django 4.1.2 on 2022-11-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='code',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
