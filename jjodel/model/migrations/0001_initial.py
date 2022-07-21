import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Model",
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
                    "is_public",
                    models.BooleanField(default=False, verbose_name="Pubblico"),
                ),
                ("content_xml", models.TextField(verbose_name="Content XML")),
                (
                    "namespace",
                    models.TextField(blank=True, null=True, verbose_name="Namespace"),
                ),
                ("name", models.TextField(verbose_name="Nome")),
            ],
        ),
        migrations.CreateModel(
            name="ModelOrgVisibility",
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
            ],
        ),
        migrations.CreateModel(
            name="ModelUserVisibility",
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
            ],
        ),
        migrations.CreateModel(
            name="ModelViewpoint",
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
                    "model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="model.model"
                    ),
                ),
            ],
        ),
    ]
