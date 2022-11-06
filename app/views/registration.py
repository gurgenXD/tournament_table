from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models.teams import Team
from app.models.tournaments import Tournament
from app.serializers.registration import TeamRegistrationSerializer


class TeamRegistration(APIView):
    @swagger_auto_schema(request_body=TeamRegistrationSerializer)
    def post(self, request, pk):
        """Регистрация на турнир."""
        serializer = TeamRegistrationSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        tournament = get_object_or_404(Tournament, pk=pk)
        team, _ = Team.objects.get_or_create(
            name=serializer.data.pop("name"), defaults=serializer.data
        )
        tournament.teams.add(team)

        return Response(status=status.HTTP_204_NO_CONTENT)
