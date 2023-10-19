# Generated by Django 4.2.6 on 2023-10-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exercise", "0003_displacement_equipment_goal_placementposition_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Organ",
            fields=[
                ("name", models.CharField(max_length=100)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Target",
            fields=[
                ("name", models.CharField(max_length=100)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name="exercise",
            name="keywords",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name="exercise",
            name="accessories",
        ),
        migrations.RemoveField(
            model_name="exercise",
            name="displacement",
        ),
        migrations.RemoveField(
            model_name="exercise",
            name="placement_position",
        ),
        migrations.RemoveField(
            model_name="exercise",
            name="target",
        ),
        migrations.RemoveField(
            model_name="exercise",
            name="target_organs",
        ),
        migrations.AddField(
            model_name="exercise",
            name="accessories",
            field=models.ManyToManyField(blank=True, to="exercise.equipment"),
        ),
        migrations.AddField(
            model_name="exercise",
            name="displacement",
            field=models.ManyToManyField(blank=True, to="exercise.displacement"),
        ),
        migrations.AddField(
            model_name="exercise",
            name="placement_position",
            field=models.ManyToManyField(blank=True, to="exercise.placementposition"),
        ),
        migrations.AddField(
            model_name="exercise",
            name="target",
            field=models.ManyToManyField(blank=True, to="exercise.target"),
        ),
        migrations.AddField(
            model_name="exercise",
            name="target_organs",
            field=models.ManyToManyField(blank=True, to="exercise.organ"),
        ),
    ]