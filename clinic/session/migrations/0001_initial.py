# Generated by Django 5.0.2 on 2024-02-13 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("patient", "0001_initial"),
        ("prescription", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Session",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                (
                    "session_type",
                    models.CharField(
                        choices=[("online", "online"), ("offline", "offline")],
                        max_length=7,
                        null=True,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("p", "pending"), ("c", "completed")], max_length=1
                    ),
                ),
                ("rate", models.IntegerField()),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patient.patient",
                    ),
                ),
                (
                    "prescription",
                    models.ManyToManyField(to="prescription.prescription"),
                ),
            ],
        ),
    ]
