from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jjodel', '0011_rename_ispublic_model_is_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uservisibility',
            name='model',
        ),
        migrations.RemoveField(
            model_name='uservisibility',
            name='user',
        ),
        migrations.AlterField(
            model_name='viewrequirement',
            name='oclString',
            field=models.TextField(verbose_name='Stringa ocl'),
        ),
        migrations.DeleteModel(
            name='OrganizationVisibility',
        ),
        migrations.DeleteModel(
            name='UserVisibility',
        ),
    ]
