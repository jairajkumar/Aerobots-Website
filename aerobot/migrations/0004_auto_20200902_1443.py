# Generated by Django 3.1 on 2020-09-02 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerobot', '0003_sponsers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsers',
            name='link',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
