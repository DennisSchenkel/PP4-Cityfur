# Generated by Django 4.2.13 on 2024-06-23 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Reports",
            new_name="Report",
        ),
    ]
