# Generated by Django 2.2.4 on 2019-11-17 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvback', '0005_movie_identifier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('idComment', models.AutoField(primary_key=True, serialize=False)),
                ('idMovie', models.IntegerField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='RecommendedMovie',
        ),
    ]
