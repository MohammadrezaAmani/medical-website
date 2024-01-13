# Generated by Django 4.2.8 on 2024-01-13 13:55

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("doctor", "0001_initial"),
        ("injury", "0001_initial"),
        ("insurance", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PateintDoctor",
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
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="doctor.doctor"
                    ),
                ),
                ("injury", models.ManyToManyField(to="injury.injury")),
            ],
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "medical_documents",
                    models.FileField(
                        blank=True, null=True, upload_to="files/documents/"
                    ),
                ),
                ("blood_type", models.CharField(blank=True, max_length=10, null=True)),
                ("height", models.FloatField(blank=True, null=True)),
                ("weight", models.FloatField(blank=True, null=True)),
                (
                    "doctor",
                    models.ManyToManyField(
                        through="patient.PateintDoctor", to="doctor.doctor"
                    ),
                ),
                (
                    "insurance",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="insurance.insurance",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("auth.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name="pateintdoctor",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="patient.patient"
            ),
        ),
    ]
