from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.serializers.teams import TeamSerializer


class TeamList(APIView):
    @swagger_auto_schema(
        request_body=TeamSerializer,
        responses={status.HTTP_201_CREATED: TeamSerializer()},
    )
    def post(self, request):
        """Создать команду."""
        serializer = TeamSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
