# Generated by Django 2.1.7 on 2019-03-22 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testaments', '0003_auto_20190322_0850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testament',
            old_name='author',
            new_name='name',
        ),
    ]
