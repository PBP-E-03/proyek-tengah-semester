# Generated by Django 4.1.2 on 2022-10-30 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default=None, null=True)),
                ('phone', models.TextField(blank=True, default=None, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('region', models.TextField()),
                ('country', models.TextField()),
                ('hopes', models.TextField()),
                ('donate_for_someone', models.BooleanField()),
                ('payment', models.ImageField(blank=True, default=None, null=True, upload_to='images')),
                ('person', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='donation.person')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
