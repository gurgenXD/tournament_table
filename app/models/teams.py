from django.db import models


class Team(models.Model):
    """Команда."""

    name = models.CharField(max_length=32, unique=True)

    class Meta:
        db_table = "teams"
