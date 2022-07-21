from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('model', '0001_initial'),
        ('viewpoint', '0001_initial'),
        ('organization', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='modelviewpoint',
            name='viewpoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewpoint.viewpoint'),
        ),
        migrations.AddField(
            model_name='modeluservisibility',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.model'),
        ),
        migrations.AddField(
            model_name='modeluservisibility',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='modelorgvisibility',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.model'),
        ),
        migrations.AddField(
            model_name='modelorgvisibility',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization'),
        ),
        migrations.AddField(
            model_name='model',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='model',
            name='instanceOf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='model.model'),
        ),
    ]
