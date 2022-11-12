from django.db import models


class Team(models.Model):
    """Команда."""

    name = models.CharField(max_length=32, unique=True)
    players = models.ManyToManyField(
        "User", related_name="teams", db_table="teams_users"
    )

    class Meta:
        db_table = "teams"
