from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from app.views import TeamRegistration, TournamentDetail, TournamentList

schema_view = get_schema_view(
    openapi.Info(title="Tournament Table API", default_version="1.0.0")
)

urlpatterns = [
    path("api/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"),
]

urlpatterns += [
    path("api/tournaments/", TournamentList.as_view(), name="tournaments"),
    path("api/tournaments/<pk>/", TournamentDetail.as_view(), name="tournament"),
    path(
        "api/tournaments/<pk>/team/",
        TeamRegistration.as_view(),
        name="team_registration",
    ),
]
