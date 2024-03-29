# Generated by Django 5.0.2 on 2024-02-13 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("exercise", "0001_initial"),
        ("patient", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prescription",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("repeat", models.IntegerField(blank=True, default=1, null=True)),
                ("sets", models.IntegerField(blank=True, default=1, null=True)),
                ("hold_time", models.IntegerField(blank=True, default=1, null=True)),
                ("total_time", models.IntegerField(blank=True, default=1, null=True)),
                ("rest_time", models.IntegerField(blank=True, default=1, null=True)),
                (
                    "exercises",
                    models.ManyToManyField(blank=True, to="exercise.exercise"),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patient.patient",
                    ),
                ),
            ],
        ),
    ]
