# Generated by Django 5.0.6 on 2024-07-08 14:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filmwork',
            options={'verbose_name': 'Film work', 'verbose_name_plural': 'Films'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Genre', 'verbose_name_plural': 'Genres'},
        ),
        migrations.AlterModelOptions(
            name='genrefilmwork',
            options={'verbose_name': 'Genre film work', 'verbose_name_plural': 'Genres films'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Person', 'verbose_name_plural': 'Persons'},
        ),
        migrations.AlterModelOptions(
            name='personfilmwork',
            options={'verbose_name': 'Person film work', 'verbose_name_plural': 'Persons films'},
        ),
        migrations.AddField(
            model_name='filmwork',
            name='file_path',
            field=models.FileField(blank=True, null=True, upload_to='movies/', verbose_name='file'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='creation_date',
            field=models.DateField(blank=True, null=True, verbose_name='creation_date'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='rating',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='rating'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='type',
            field=models.CharField(choices=[('MV', 'movie'), ('TV', 'tv_show')], default='MV', max_length=20, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.TextField(verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='personfilmwork',
            name='role',
            field=models.CharField(choices=[('AR', 'Actor'), ('PR', 'Producer'), ('ST', 'Scenarist')], default='AR', verbose_name='role'),
        ),
        migrations.AddConstraint(
            model_name='genrefilmwork',
            constraint=models.UniqueConstraint(fields=('film_work_id', 'genre_id'), name='unique_genre_film_work'),
        ),
        migrations.AddConstraint(
            model_name='personfilmwork',
            constraint=models.UniqueConstraint(fields=('film_work_id', 'person_id', 'role'), name='idx_person_film_work_unique'),
        ),
    ]
