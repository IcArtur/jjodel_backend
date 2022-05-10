from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jjodel", "0003_alter_organization_openmembership_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organization",
            name="bio",
            field=models.TextField(blank=True, null=True, verbose_name="Bio"),
        ),
        migrations.AlterField(
            model_name="organization",
            name="mailDomainRequired",
            field=models.TextField(blank=True, null=True, verbose_name="Mail Domain"),
        ),
    ]
