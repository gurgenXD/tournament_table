from django.db import models


class User(models.Model):
    """Пользователь."""

    name = models.CharField(max_length=32, unique=True)

    class Meta:
        db_table = "users"
