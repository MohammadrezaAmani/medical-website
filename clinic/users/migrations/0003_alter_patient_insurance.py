# Generated by Django 5.0.2 on 2024-02-13 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("insurance", "0001_initial"),
        ("users", "0002_doctor_pateintdoctor_patient_pateintdoctor_patient"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="insurance",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="insurance.insurance",
            ),
        ),
    ]
