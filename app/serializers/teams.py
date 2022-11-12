from rest_framework import serializers

from app.models.teams import Team
from app.validators import validate_players_count


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name", "players"]

    def validate(self, data):
        """Провалидировать длину участников команды."""
        validate_players_count(data["players"])

        super().validate(data)

        return data
