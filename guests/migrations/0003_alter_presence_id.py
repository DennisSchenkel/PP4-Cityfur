# Generated by Django 4.2.11 on 2024-05-09 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("guests", "0002_presence"),
    ]

    operations = [
        migrations.AlterField(
            model_name="presence",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
