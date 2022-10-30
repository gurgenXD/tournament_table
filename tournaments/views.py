from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tournaments.models import Tournament
from tournaments.serializers import (TournamentCreateSerializer,
                                     TournamentReadSerializer)


class TournamentList(APIView):
    @swagger_auto_schema(responses={status.HTTP_200_OK: TournamentReadSerializer()})
    def get(self, _request):
        """Получить список турниров."""
        tournaments = Tournament.objects.all()
        serializer = TournamentReadSerializer(tournaments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=TournamentCreateSerializer,
        responses={status.HTTP_201_CREATED: TournamentReadSerializer()},
    )
    def post(self, request):
        """Создать турнир."""
        serializer = TournamentCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TournamentDetail(APIView):
    @swagger_auto_schema(responses={status.HTTP_200_OK: TournamentReadSerializer()})
    def get(self, _request, pk):
        """Получить турнир."""
        try:
            tournament = Tournament.objects.get(pk=pk)
        except Tournament.DoesNotExist:
            raise Http404

        serializer = TournamentReadSerializer(tournament)
        return Response(serializer.data, status=status.HTTP_200_OK)
