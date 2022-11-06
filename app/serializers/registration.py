from rest_framework import serializers


class TeamRegistrationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=32)
