# Generated by Django 4.2.6 on 2023-10-19 08:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patient", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="patient",
            name="user",
        ),
        migrations.AddField(
            model_name="patient",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="patient",
            name="last_name",
            field=models.CharField(default="amani", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="patient",
            name="name",
            field=models.CharField(default="amani", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="patient",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
