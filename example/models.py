from django.db import models
import uuid


# City model
class City(models.Model):
    cityId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# User model
class User(models.Model):
    userId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=300)
    salt = models.CharField(max_length=32, null=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    cityId = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username

# Category model
class Category(models.Model):
    categoryId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

# Media model
class Media(models.Model):
    mediaId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    categoryId = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    releaseYear = models.BigIntegerField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Song model
class Song(models.Model):
    songId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mediaId = models.OneToOneField(Media, on_delete=models.CASCADE)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    length = models.BigIntegerField()

    def __str__(self):
        return str(self.mediaId)

# Book model
class Book(models.Model):
    bookId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mediaId = models.OneToOneField(Media, on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return str(self.mediaId)

# Movie model
class Movie(models.Model):
    movieId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mediaId = models.OneToOneField(Media, on_delete=models.CASCADE)
    director = models.CharField(max_length=100)
    cast = models.TextField()
    length = models.BigIntegerField()
    description = models.TextField()
    screenwriters = models.CharField(max_length=100)

    def __str__(self):
        return str(self.mediaId)

# Play model
class Play(models.Model):
    playId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mediaId = models.OneToOneField(Media, on_delete=models.CASCADE)
    director = models.CharField(max_length=100)
    cast = models.TextField()
    length = models.BigIntegerField()
    description = models.TextField()
    screenwriters = models.CharField(max_length=100)

    def __str__(self):
        return str(self.mediaId)

# TV Show model
class Tvshow(models.Model):
    tvshowId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mediaId = models.OneToOneField(Media, on_delete=models.CASCADE)
    noOfSeasons = models.BigIntegerField()
    noOfEpisodes = models.BigIntegerField()
    director = models.CharField(max_length=100)
    cast = models.TextField()
    description = models.TextField()
    screenwriters = models.CharField(max_length=100)

    def __str__(self):
        return str(self.mediaId)
