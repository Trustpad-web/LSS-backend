# Generated by Django 4.2.5 on 2023-11-25 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_inventory_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadata',
            name='value',
            field=models.CharField(max_length=500),
        ),
    ]
