from rest_framework import serializers

PLAYERS_MAX_COUNT = 2


def validate_players_count(value):
    """Провалидировать кол-во игроков в команде."""
    if len(value) != PLAYERS_MAX_COUNT:
        raise serializers.ValidationError(
            f"players count need to be {PLAYERS_MAX_COUNT}"
        )
