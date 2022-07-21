import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("organization", "0001_initial"),
        ("view", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Viewpoint",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Nome")),
                (
                    "is_public",
                    models.BooleanField(default=False, verbose_name="Pubblico"),
                ),
                (
                    "coordinates",
                    models.JSONField(blank=True, null=True, verbose_name="Coordinate"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ViewpointView",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "view",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="view.view"
                    ),
                ),
                (
                    "viewpoint",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="viewpoint.viewpoint",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ViewpointUserVisibility",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "readonly",
                    models.BooleanField(default=True, verbose_name="Sola lettura"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "viewpoint",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="viewpoint.viewpoint",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ViewpointOrgVisibility",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "readonly",
                    models.BooleanField(default=True, verbose_name="Sola lettura"),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organization.organization",
                    ),
                ),
                (
                    "viewpoint",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="viewpoint.viewpoint",
                    ),
                ),
            ],
        ),
    ]
