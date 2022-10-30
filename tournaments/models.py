from django.db import models


class Tournament(models.Model):
    """Турнир."""

    class TournamentStatuses(models.TextChoices):
        OPENED = "OPENED"
        ACTIVE = "ACTIVE"
        FINISHED = "FINISHED"

    name = models.CharField(max_length=64)
    status = models.CharField(
        max_length=8,
        choices=TournamentStatuses.choices,
        default=TournamentStatuses.OPENED,
    )
