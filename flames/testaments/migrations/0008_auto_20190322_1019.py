# Generated by Django 2.1.7 on 2019-03-22 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testaments', '0007_auto_20190322_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testament',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='testament',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='testament',
            name='user',
        ),
        migrations.AddField(
            model_name='testament',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
