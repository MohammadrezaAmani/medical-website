# Generated by Django 4.2.6 on 2023-10-19 08:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("doctor", "0002_doctor_bio_doctor_created_at_doctor_last_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="doctor",
            name="user",
        ),
    ]