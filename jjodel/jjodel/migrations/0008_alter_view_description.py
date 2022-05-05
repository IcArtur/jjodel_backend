from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jjodel', '0007_view_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descrizione'),
        ),
    ]
