# Generated by Django 3.1 on 2020-09-02 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerobot', '0009_delete_sponsers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('link', models.CharField(max_length=10000, null=True)),
            ],
            options={
                'verbose_name': 'Sponsers',
                'verbose_name_plural': 'Sponsers',
            },
        ),
    ]