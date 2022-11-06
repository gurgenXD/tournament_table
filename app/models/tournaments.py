from django.db import models


class TournamentStatuses(models.TextChoices):
    OPENED = "OPENED"
    ACTIVE = "ACTIVE"
    FINISHED = "FINISHED"


class Tournament(models.Model):
    """Турнир."""

    name = models.CharField(max_length=64, unique=True)
    status = models.CharField(
        max_length=8,
        choices=TournamentStatuses.choices,
        default=TournamentStatuses.OPENED,
    )
    teams = models.ManyToManyField(
        "Team", related_name="tournaments", db_table="tournaments_teams"
    )

    class Meta:
        db_table = "tournaments"
