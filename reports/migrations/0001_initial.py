# Generated by Django 4.2.11 on 2024-05-01 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reports",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("report_date", models.DateField(auto_now_add=True)),
                ("report_text", models.TextField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["report_date"],
            },
        ),
    ]
