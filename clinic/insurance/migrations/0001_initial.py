# Generated by Django 5.0.2 on 2024-02-13 08:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Insurance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("insurance_name", models.CharField(max_length=100)),
                ("insurance_description", models.CharField(max_length=100)),
            ],
        ),
    ]
