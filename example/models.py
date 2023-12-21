from django.db import models
import uuid


# City model
class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# User model
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=300)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username

# Universal media model, used as a superclass for specific media types
class Media(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    rating = models.IntegerField()
    year = models.IntegerField()

# Song model
class Song(Media):
    performer = models.CharField(max_length=100)

# Book model
class Book(Media):
    writer = models.CharField(max_length=100)

# Movie model
class Movie(Media):
    director = models.CharField(max_length=100)