# Generated by Django 4.2.8 on 2024-01-13 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("session", "0001_initial"),
        ("prescription", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrescriptionReport",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("repeats", models.FloatField()),
                ("pain_level", models.FloatField()),
                ("hardness_present", models.FloatField()),
                ("additional_notes", models.TextField(blank=True, null=True)),
                (
                    "prescription",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="prescription.prescription",
                    ),
                ),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="session.session",
                    ),
                ),
            ],
        ),
    ]
