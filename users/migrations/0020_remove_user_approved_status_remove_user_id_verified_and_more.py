# Generated by Django 4.2.5 on 2023-10-31 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_user_auth_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='approved_status',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id_verified',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_approved',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mail_verified',
        ),
    ]
