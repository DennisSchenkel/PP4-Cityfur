# Generated by Django 4.2.13 on 2024-07-04 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("guests", "0006_presence_pickup_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="presence",
            name="pickup",
        ),
    ]