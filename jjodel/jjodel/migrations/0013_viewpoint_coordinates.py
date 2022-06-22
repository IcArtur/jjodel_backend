from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jjodel', '0012_remove_uservisibility_model_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewpoint',
            name='coordinates',
            field=models.JSONField(blank=True, null=True, verbose_name='Coordinate'),
        ),
    ]
