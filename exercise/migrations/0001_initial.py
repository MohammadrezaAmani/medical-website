# Generated by Django 4.2.6 on 2023-10-19 09:53

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Exercise",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("video", models.FileField(blank=True, null=True, upload_to="videos/")),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("others", models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
