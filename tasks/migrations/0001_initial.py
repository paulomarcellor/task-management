# Generated by Django 4.2.11 on 2024-04-18 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="dataTask",
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
                ("name", models.CharField(max_length=200)),
                ("category", models.CharField(max_length=200)),
                ("start", models.DateField()),
                ("deadline", models.DateField()),
                ("status", models.CharField(max_length=100)),
                ("aap", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="stepsTask",
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
                ("step", models.CharField(max_length=200)),
                ("step_start", models.DateField()),
                ("step_end", models.DateField()),
                ("done", models.BooleanField(default=False)),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tasks.datatask"
                    ),
                ),
            ],
        ),
    ]
