from http import HTTPStatus

from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from tournaments.models import Tournament
from tournaments.serializers import TournamentsReadSerializer


class ListTournamentsView(APIView):
    @swagger_auto_schema(responses={HTTPStatus.OK.value: TournamentsReadSerializer()})
    def get(self, request, format=None):
        """Получить список турниров."""
        Tournament.objects.create(
            name="Tournament1",
        )
        tournaments = Tournament.objects.all()
        return Response(tournaments)
