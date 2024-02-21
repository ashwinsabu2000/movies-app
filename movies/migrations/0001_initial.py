# Generated by Django 2.1.15 on 2024-01-31 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=30)),
                ('release_date', models.DateTimeField(verbose_name='release date')),
                ('genre', models.CharField(max_length=200)),
                ('duration', models.FloatField()),
            ],
        ),
    ]
