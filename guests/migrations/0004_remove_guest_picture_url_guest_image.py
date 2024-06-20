# Generated by Django 4.2.11 on 2024-05-19 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("guests", "0003_alter_presence_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="guest",
            name="picture_url",
        ),
        migrations.AddField(
            model_name="guest",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]