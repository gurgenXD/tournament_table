from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models.teams import Team
from app.models.tournaments import Tournament, TournamentStatuses
from app.serializers.tournaments import (TournamentSerializer,
                                         TournamentStartSerializer,
                                         TournamentTableSerializer)


class TournamentList(APIView):
    @swagger_auto_schema(responses={status.HTTP_200_OK: TournamentSerializer()})
    def get(self, _request):
        """Получить список турниров."""
        tournaments = Tournament.objects.all()
        serializer = TournamentSerializer(tournaments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=TournamentSerializer,
        responses={status.HTTP_201_CREATED: TournamentSerializer()},
    )
    def post(self, request):
        """Создать турнир."""
        serializer = TournamentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TournamentDetail(APIView):
    @swagger_auto_schema(responses={status.HTTP_200_OK: TournamentSerializer()})
    def get(self, _request, id):
        """Получить турнир."""
        tournament = get_object_or_404(Tournament, id=id)

        serializer = TournamentSerializer(tournament)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=TournamentStartSerializer)
    def patch(self, request, id):
        """Обновить статус турнира."""
        tournament = get_object_or_404(Tournament, id=id)

        serializer = TournamentStartSerializer(
            tournament, data=request.data, partial=True
        )

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TournamentParticipantDetail(APIView):
    def post(self, _request, id, team_id):
        """Добавление участника на турнир."""
        tournament = get_object_or_404(Tournament, id=id)
        team = get_object_or_404(Team, id=team_id)

        tournament.participants.add(team)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, _request, id, team_id):
        """Удаление участника из турнира."""
        tournament = get_object_or_404(Tournament, id=id)
        team = get_object_or_404(Team, id=team_id)

        tournament.participants.remove(team)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TournamentTableDetail(APIView):
    @swagger_auto_schema(responses={status.HTTP_200_OK: TournamentTableSerializer()})
    def get(self, _request, id):
        """Получить турнирную таблицу."""
        tournament = get_object_or_404(
            Tournament, id=id, status=TournamentStatuses.ACTIVE
        )

        serializer = TournamentTableSerializer(tournament)

        return Response(serializer.data, status=status.HTTP_200_OK)
