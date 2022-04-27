import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jjodel", "0002_alter_user_options_alter_user_managers_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organization",
            name="openMembership",
            field=models.BooleanField(default=False, verbose_name="Iscrizione Aperta"),
        ),
        migrations.AlterField(
            model_name="organization",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="jjodel.groupmember",
            ),
        ),
    ]
