# Generated by Django 4.2.11 on 2024-06-13 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("guests", "0004_remove_guest_picture_url_guest_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="presence",
            name="pickup",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="presence",
            name="report",
            field=models.BooleanField(default=False),
        ),
    ]
