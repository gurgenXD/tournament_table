from collections import defaultdict

from rest_framework import serializers

from app.models import Match, Tournament


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ["id", "name", "status"]
        read_only_fields = ["id", "status"]


class TournamentStartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ["status"]


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
        data = defaultdict(list)

        for item in obj.matches.all():
            data[item.stage].append(item)

        pre_data = []
        for number, matches in data.items():
            pre_data.append({"number": number, "matches": matches})

        return TournamentStageSerializer(pre_data, many=True).data
