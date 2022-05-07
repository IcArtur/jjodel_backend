from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jjodel', '0009_viewpointuservisibility'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelUserVisibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('readonly', models.BooleanField(default=True, verbose_name='Sola lettura')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jjodel.model')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ModelOrgVisibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('readonly', models.BooleanField(default=True, verbose_name='Sola lettura')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jjodel.model')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jjodel.organization')),
            ],
        ),
    ]
