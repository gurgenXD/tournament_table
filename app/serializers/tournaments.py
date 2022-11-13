from rest_framework import serializers

from app.models.tournaments import Tournament


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ["id", "name", "status"]
        read_only_fields = ["id", "status"]


class TournamentStartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ["status"]
