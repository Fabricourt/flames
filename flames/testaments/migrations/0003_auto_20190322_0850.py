# Generated by Django 2.1.7 on 2019-03-22 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testaments', '0002_auto_20190322_0841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testament',
            old_name='name',
            new_name='author',
        ),
    ]
