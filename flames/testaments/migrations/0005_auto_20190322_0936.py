# Generated by Django 2.1.7 on 2019-03-22 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testaments', '0004_auto_20190322_0922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testament',
            old_name='name',
            new_name='partner',
        ),
    ]
