# Generated by Django 4.2.13 on 2024-07-05 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("guests", "0007_remove_presence_pickup"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="presence",
            name="report",
        ),
    ]
