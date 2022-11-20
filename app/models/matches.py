from django.db import models


class Match(models.Model):
    """Матч."""

    tournament = models.ForeignKey(
        "Tournament", on_delete=models.CASCADE, related_name="matches"
    )
    stage = models.PositiveSmallIntegerField()
    team1 = models.ForeignKey("Team", on_delete=models.PROTECT, related_name="matches1")
    team2 = models.ForeignKey("Team", on_delete=models.PROTECT, related_name="matches2")
    team1_score = models.PositiveSmallIntegerField(default=0)
    team2_score = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = "matches"
