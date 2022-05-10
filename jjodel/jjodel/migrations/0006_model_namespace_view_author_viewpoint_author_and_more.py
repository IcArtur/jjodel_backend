import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jjodel", "0005_alter_organization_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="model",
            name="namespace",
            field=models.TextField(blank=True, null=True, verbose_name="Namespace"),
        ),
        migrations.AddField(
            model_name="view",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="viewpoint",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="model",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="model",
            name="instanceOf",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="jjodel.model",
            ),
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
                        to="jjodel.organization",
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
    ]
