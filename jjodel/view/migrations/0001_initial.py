import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("organization", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="View",
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
                    "preview_image",
                    models.BinaryField(
                        blank=True, null=True, verbose_name="Preview Immagine"
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Descrizione"),
                ),
                (
                    "is_public",
                    models.BooleanField(default=False, verbose_name="Pubblico"),
                ),
                (
                    "html",
                    models.TextField(blank=True, null=True, verbose_name="Testo HTML"),
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
            name="ViewUserVisibility",
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
                    "view",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="view.view"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ViewRequirement",
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
                ("oclString", models.TextField(verbose_name="Stringa ocl")),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="Commento"),
                ),
                (
                    "view",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="view.view"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ViewOrgVisibility",
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
                    "view",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="view.view"
                    ),
                ),
            ],
        ),
    ]
