# Generated by Django 4.0.1 on 2022-02-16 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomm', '0012_alter_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.IntegerField(default=1),
        ),
    ]