# Generated by Django 3.1 on 2020-09-03 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aerobot', '0013_remove_gallery_link'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Gallery',
        ),
    ]