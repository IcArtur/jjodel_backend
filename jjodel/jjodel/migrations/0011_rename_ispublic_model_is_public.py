from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jjodel', '0010_modeluservisibility_modelorgvisibility'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model',
            old_name='isPublic',
            new_name='is_public',
        ),
    ]
