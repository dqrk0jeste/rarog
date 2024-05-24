from django.db import models
import uuid


# City model
class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# User model
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username

# Category model
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Media model
class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    releaseYear = models.BigIntegerField()
    genre = models.CharField(max_length=100)
    imageId = models.UUIDField(null=True)

    def __str__(self):
        return str(self.id)

# Song model
class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    media = models.OneToOneField(Media, on_delete=models.CASCADE)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    length = models.BigIntegerField()

    def __str__(self):
        return str(self.id)

# Book model
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    media = models.OneToOneField(Media, on_delete=models.CASCADE)
    authors = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return str(self.id)

# Movie model
class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    media = models.OneToOneField(Media, on_delete=models.CASCADE)
    director = models.CharField(max_length=100)
    cast = models.TextField()
    length = models.BigIntegerField()
    description = models.TextField()
    screenwriters = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

# Play model
class Play(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    media = models.OneToOneField(Media, on_delete=models.CASCADE)
    director = models.CharField(max_length=100)
    cast = models.TextField()
    length = models.BigIntegerField()
    description = models.TextField()
    screenwriters = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

# TV Show model
class Tvshow(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    media = models.OneToOneField(Media, on_delete=models.CASCADE)
    noOfSeasons = models.BigIntegerField()
    noOfEpisodes = models.BigIntegerField()
    director = models.CharField(max_length=100)
    cast = models.TextField()
    description = models.TextField()
    screenwriters = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

# Media rating model
class Rating(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.SmallIntegerField()
    
    def __str__(self):
        return str(self.id)