from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jjodel", "0006_model_namespace_view_author_viewpoint_author_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="view",
            name="name",
            field=models.CharField(default="view", max_length=255, verbose_name="Nome"),
            preserve_default=False,
        ),
    ]
