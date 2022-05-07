from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jjodel', '0008_alter_view_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewpointUserVisibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('readonly', models.BooleanField(default=True, verbose_name='Sola lettura')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('viewpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jjodel.viewpoint')),
            ],
        ),
    ]
