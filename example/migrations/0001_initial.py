# Generated by Django 4.1.3 on 2024-02-12 18:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('cityId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('mediaId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('releaseYear', models.BigIntegerField()),
                ('genre', models.CharField(max_length=100)),
                ('categoryId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='example.category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cityId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='example.city')),
            ],
        ),
        migrations.CreateModel(
            name='Tvshow',
            fields=[
                ('tvshowId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('noOfSeasons', models.BigIntegerField()),
                ('noOfEpisodes', models.BigIntegerField()),
                ('director', models.CharField(max_length=100)),
                ('cast', models.TextField()),
                ('description', models.TextField()),
                ('screenwriters', models.CharField(max_length=100)),
                ('mediaId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='example.media')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('songId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('artist', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('length', models.BigIntegerField()),
                ('mediaId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='example.media')),
            ],
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('playId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('director', models.CharField(max_length=100)),
                ('cast', models.TextField()),
                ('length', models.BigIntegerField()),
                ('description', models.TextField()),
                ('screenwriters', models.CharField(max_length=100)),
                ('mediaId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='example.media')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movieId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('director', models.CharField(max_length=100)),
                ('cast', models.TextField()),
                ('length', models.BigIntegerField()),
                ('description', models.TextField()),
                ('screenwriters', models.CharField(max_length=100)),
                ('mediaId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='example.media')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('autor', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('mediaId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='example.media')),
            ],
        ),
    ]