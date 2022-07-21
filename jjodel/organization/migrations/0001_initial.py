from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Organization",
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
                    "isPublic",
                    models.BooleanField(default=False, verbose_name="Pubblico"),
                ),
                (
                    "openMembership",
                    models.BooleanField(
                        default=False, verbose_name="Iscrizione Aperta"
                    ),
                ),
                ("name", models.TextField(verbose_name="Nome")),
                (
                    "mailDomainRequired",
                    models.TextField(blank=True, null=True, verbose_name="Mail Domain"),
                ),
                ("bio", models.TextField(blank=True, null=True, verbose_name="Bio")),
            ],
        ),
    ]
