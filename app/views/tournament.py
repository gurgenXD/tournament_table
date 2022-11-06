from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models.tournaments import Tournament
from app.serializers.tournaments import TournamentReadSerializer


class TournamentDetail(APIView):
    @swagger_auto_schema(responses={status.HTTP_200_OK: TournamentReadSerializer()})
    def get(self, _request, pk):
        """Получить турнир."""
        tournament = get_object_or_404(Tournament, pk=pk)

        serializer = TournamentReadSerializer(tournament)
        return Response(serializer.data, status=status.HTTP_200_OK)
