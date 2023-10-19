# Generated by Django 4.2.6 on 2023-10-19 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("doctor", "0003_remove_doctor_user"),
        ("patient", "0002_remove_patient_user_patient_bio_patient_last_name_and_more"),
        ("exercise", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Drug",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("others", models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Prescription",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="doctor.doctor"
                    ),
                ),
                ("drugs", models.ManyToManyField(blank=True, to="prescription.drug")),
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