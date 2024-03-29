# Generated by Django 4.1.3 on 2024-03-03 20:00

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
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('releaseYear', models.BigIntegerField()),
                ('genre', models.CharField(max_length=100)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='example.category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='example.city')),
            ],
        ),
        migrations.CreateModel(
            name='Tvshow',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('noOfSeasons', models.BigIntegerField()),
                ('noOfEpisodes', models.BigIntegerField()),
                ('director', models.CharField(max_length=100)),
                ('cast', models.TextField()),
                ('description', models.TextField()),
                ('screenwriters', models.CharField(max_length=100)),
                ('media', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='example.media')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('artist', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('length', models.BigIntegerField()),
                ('media', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='example.media')),
            ],
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('director', models.CharField(max_length=100)),
                ('cast', models.TextField()),
                ('length', models.BigIntegerField()),
                ('description', models.TextField()),
                ('screenwriters', models.CharField(max_length=100)),
                ('media', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='example.media')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('director', models.CharField(max_length=100)),
                ('cast', models.TextField()),
                ('length', models.BigIntegerField()),
                ('description', models.TextField()),
                ('screenwriters', models.CharField(max_length=100)),
                ('media', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='example.media')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('authors', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('media', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='example.media')),
            ],
        ),
    ]
