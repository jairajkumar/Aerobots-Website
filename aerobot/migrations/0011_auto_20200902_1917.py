# Generated by Django 3.1 on 2020-09-02 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerobot', '0010_sponsers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='link',
            field=models.CharField(max_length=100000000, null=True),
        ),
    ]