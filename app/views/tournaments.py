from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models.tournaments import Tournament
from app.serializers.tournaments import (TournamentCreateSerializer,
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

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
