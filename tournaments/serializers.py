from django.db import transaction
from django.utils import timezone
from rest_framework import serializers

from tournaments.models import Tournament


class TournamentsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = "__all__"
