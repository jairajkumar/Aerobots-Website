# Generated by Django 3.1 on 2020-09-02 08:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=2000)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='meals/')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]
