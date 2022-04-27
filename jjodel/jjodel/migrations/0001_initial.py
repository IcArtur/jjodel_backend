import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GroupMember",
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
                ("since", models.DateField(blank=True, editable=False, null=True)),
            ],
        ),
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
                    "isPublic",
                    models.BooleanField(default=False, verbose_name="Pubblico"),
                ),
                ("content_xml", models.TextField(verbose_name="Content XML")),
                ("name", models.TextField(verbose_name="Nome")),
            ],
        ),
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
                    models.BooleanField(default=False, verbose_name="Pubblico"),
                ),
                ("name", models.TextField(verbose_name="Nome")),
                ("mailDomainRequired", models.TextField(verbose_name="Mail Domain")),
                ("bio", models.TextField(verbose_name="Bio")),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jjodel.groupmember",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                    "mail",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="Email"
                    ),
                ),
                ("name", models.TextField(blank=True, null=True, verbose_name="Nome")),
                (
                    "surname",
                    models.TextField(blank=True, null=True, verbose_name="Cognome"),
                ),
                ("password", models.TextField(verbose_name="Password")),
                ("username", models.TextField(verbose_name="Username")),
                ("bio", models.TextField(blank=True, null=True, verbose_name="Bio")),
            ],
        ),
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
                (
                    "preview_image",
                    models.BinaryField(
                        blank=True, null=True, verbose_name="Preview Immagine"
                    ),
                ),
                ("description", models.TextField(verbose_name="Descrizione")),
                (
                    "is_public",
                    models.BooleanField(default=False, verbose_name="Pubblico"),
                ),
                (
                    "html",
                    models.TextField(blank=True, null=True, verbose_name="Testo HTML"),
                ),
            ],
        ),
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
                        on_delete=django.db.models.deletion.CASCADE, to="jjodel.user"
                    ),
                ),
                (
                    "view",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jjodel.view"
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
                ("oclString", models.TextField(verbose_name="Commento")),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="Commento"),
                ),
                (
                    "view",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jjodel.view"
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
                        on_delete=django.db.models.deletion.CASCADE, to="jjodel.view"
                    ),
                ),
                (
                    "viewpoint",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jjodel.viewpoint",
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
                        to="jjodel.organization",
                    ),
                ),
                (
                    "view",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jjodel.view"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserVisibility",
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
                    "model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jjodel.model"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jjodel.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrganizationVisibility",
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
                    "model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jjodel.model"
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jjodel.organization",
                    ),
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
                        on_delete=django.db.models.deletion.CASCADE, to="jjodel.model"
                    ),
                ),
                (
                    "viewpoint",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jjodel.viewpoint",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="model",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="jjodel.user"
            ),
        ),
        migrations.AddField(
            model_name="model",
            name="instanceOf",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="jjodel.model"
            ),
        ),
        migrations.CreateModel(
            name="MembershipRequest",
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
                ("sent", models.DateField(blank=True, editable=False, null=True)),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jjodel.user"
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jjodel.organization",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="groupmember",
            name="member",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="jjodel.user"
            ),
        ),
        migrations.AddField(
            model_name="groupmember",
            name="organization_fk",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="jjodel.organization"
            ),
        ),
        migrations.CreateModel(
            name="AdminMember",
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
                ("since", models.DateField(blank=True, editable=False, null=True)),
                (
                    "admin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jjodel.user"
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jjodel.organization",
                    ),
                ),
            ],
        ),
    ]
