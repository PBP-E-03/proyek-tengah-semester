# Generated by Django 4.1.2 on 2022-11-02 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_rename_username_user_name_user_groups_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]
