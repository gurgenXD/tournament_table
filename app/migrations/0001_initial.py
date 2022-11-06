# Generated by Django 4.1.2 on 2022-11-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Team",
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
                ("name", models.CharField(max_length=32, unique=True)),
            ],
            options={
                "db_table": "teams",
            },
        ),
        migrations.CreateModel(
            name="Tournament",
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
                ("name", models.CharField(max_length=64, unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("OPENED", "Opened"),
                            ("ACTIVE", "Active"),
                            ("FINISHED", "Finished"),
                        ],
                        default="OPENED",
                        max_length=8,
                    ),
                ),
                (
                    "teams",
                    models.ManyToManyField(
                        db_table="tournaments_teams",
                        related_name="tournaments",
                        to="app.team",
                    ),
                ),
            ],
            options={
                "db_table": "tournaments",
            },
        ),
    ]