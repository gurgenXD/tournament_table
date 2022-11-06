from rest_framework import serializers

from app.models.tournaments import Tournament


class TournamentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ["name"]


class TournamentReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ["id", "name", "status"]
