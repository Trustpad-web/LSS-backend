# Generated by Django 4.2.5 on 2023-11-01 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_user_auth_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='auth_token',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
