# Generated by Django 5.0.6 on 2024-06-10 10:15

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE SCHEMA IF NOT EXISTS content;
            """
        ),
        migrations.CreateModel(
            name='FilmWork',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.TextField(verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('creation_date', models.DateField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True,
                                             validators=[django.core.validators.MinValueValidator(0),
                                                         django.core.validators.MaxValueValidator(100)])),
                ('type', models.CharField(choices=[('MV', 'movie'), ('TV', 'tv_show')], default='MV', max_length=2)),
            ],
            options={
                'verbose_name': 'Кинопроизведение',
                'verbose_name_plural': 'Кинопроизведения',
                'db_table': 'content"."film_work',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'db_table': 'content"."genre',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.TextField(max_length=255, verbose_name='full_name')),
            ],
            options={
                'verbose_name': 'Персонаж',
                'verbose_name_plural': 'Персонажи',
                'db_table': 'content"."person',
            },
        ),
        migrations.CreateModel(
            name='GenreFilmWork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
            ],
            options={
                'verbose_name': 'Жанр кинопроизведения',
                'verbose_name_plural': 'Жанры кинопроизведения',
                'db_table': 'content"."genre_film_work',
            },
        ),
        migrations.AddField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(through='movies.GenreFilmWork', to='movies.genre'),
        ),
        migrations.CreateModel(
            name='PersonFilmWork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role', models.TextField(verbose_name='role')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person')),
            ],
            options={
                'verbose_name': 'Персонаж кинопроизведения',
                'verbose_name_plural': 'Персонажи кинопроизведения',
                'db_table': 'content"."person_film_work',
            },
        ),
    ]
