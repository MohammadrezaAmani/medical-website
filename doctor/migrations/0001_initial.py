# Generated by Django 4.2.6 on 2023-10-20 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Patient",
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
                ("name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("bio", models.TextField(blank=True, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("m", "Male"), ("f", "Female")], max_length=1
                    ),
                ),
                ("birth_date", models.DateField()),
                ("address", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=10)),
                ("insurance_number", models.CharField(max_length=10)),
                ("insurance_company", models.CharField(max_length=100)),
                ("injury_date", models.DateField()),
                ("injury_description", models.CharField(max_length=100)),
                ("injury_type", models.CharField(max_length=100)),
                (
                    "medical_documents",
                    models.FileField(blank=True, null=True, upload_to="documents/"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patient_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Doctor",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("bio", models.TextField(blank=True, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("m", "Male"), ("f", "Female")], max_length=1
                    ),
                ),
                ("birth_date", models.DateField()),
                ("medical_system_code", models.CharField(max_length=10)),
                ("address", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="doctor_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
