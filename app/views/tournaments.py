from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models.tournaments import Tournament
from app.serializers.tournaments import TournamentSerializer


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
    def get(self, _request, pk):
        """Получить турнир."""
        tournament = get_object_or_404(Tournament, pk=pk)

        serializer = TournamentSerializer(tournament)
        return Response(serializer.data, status=status.HTTP_200_OK)
