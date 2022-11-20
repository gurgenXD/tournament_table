from django.core.management.base import BaseCommand, CommandError

from app.models import Team, Tournament, TournamentStatuses, User


class Command(BaseCommand):
    help = "Generate data."

    def add_arguments(self, parser):
        parser.add_argument("teams_count", type=int)

    def handle(self, *args, **options):
        """Сгенерировать данные."""
        try:
            tournament, _ = Tournament.objects.update_or_create(
                name="Tournament1", defaults={"status": TournamentStatuses.ACTIVE}
            )

            for i in range(1, options["teams_count"] + 1):
                team = self._create_teams_with_players(i)
                tournament.participants.add(team)
        except Exception as exc:
            raise CommandError(f"Error while generating data: {exc}")

        self.stdout.write(self.style.SUCCESS("Testing data was generated."))

    def _create_teams_with_players(self, postfix):
        """Создать команды."""
        team, _ = Team.objects.get_or_create(name=f"Team{postfix}")

        user1, _ = User.objects.get_or_create(name=f"User{2*postfix-1}")
        user2, _ = User.objects.get_or_create(name=f"User{2*postfix}")

        team.players.add(user1, user2)

        self.stdout.write(
            f"Team was created: id={team.id}, players=[{user1.id}, {user2.id}]"
        )

        return team
