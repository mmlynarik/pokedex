# Generated by Django 5.2.1 on 2025-05-29 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("birthdate", models.DateField(blank=True, null=True)),
                ("cv", models.FileField(blank=True, null=True, upload_to="")),
                (
                    "department",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="pokeapp.department"),
                ),
            ],
        ),
    ]
