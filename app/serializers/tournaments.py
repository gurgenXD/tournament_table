from itertools import groupby

from rest_framework import serializers

from app.models import Match, Tournament


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ["id", "name", "status"]
        read_only_fields = ["id", "status"]


class TournamentParticipantSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    score = serializers.IntegerField()


class TournamentMatchSerializer(serializers.ModelSerializer):
    participants = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = ["id", "participants"]

    def get_participants(self, obj):
        return [
            TournamentParticipantSerializer(
                {"id": obj.team1.id, "score": obj.team1_score}
            ).data,
            TournamentParticipantSerializer(
                {"id": obj.team2.id, "score": obj.team2_score}
            ).data,
        ]


class TournamentStageSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    matches = TournamentMatchSerializer(many=True, read_only=True)


class TournamentTableSerializer(serializers.ModelSerializer):
    stages = serializers.SerializerMethodField()

    class Meta:
        model = Tournament
        fields = [
            "id",
            "name",
            "status",
            "participants",
            "stages",
        ]

    def get_stages(self, obj):
        pre_data = []
        for number, matches in groupby(obj.matches.all(), key=lambda x: x.stage):
            pre_data.append({"number": number, "matches": list(matches)})

        return TournamentStageSerializer(pre_data, many=True).data
