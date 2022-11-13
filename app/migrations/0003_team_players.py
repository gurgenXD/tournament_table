# Generated by Django 4.1.2 on 2022-11-12 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="players",
            field=models.ManyToManyField(
                db_table="teams_users", related_name="teams", to="app.user"
            ),
        ),
    ]
