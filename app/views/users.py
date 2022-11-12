from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.serializers.users import UserSerializer


class UserList(APIView):
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={status.HTTP_201_CREATED: UserSerializer()},
    )
    def post(self, request):
        """Создать пользователя."""
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
