# Generated by Django 4.1.2 on 2022-11-30 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donation', '0002_alter_donation_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('rewarded_coins', models.IntegerField()),
                ('country', models.TextField()),
                ('hopes', models.TextField()),
                ('donate_for_someone', models.BooleanField()),
                ('payment', models.ImageField(default=None, upload_to='bukti_pembayaran')),
                ('person', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='donation.person')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
    ]
