from rest_framework.serializers import ModelSerializer
from example.models import *
from argon2 import PasswordHasher

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class RatingSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Rating
        fields = ['id', 'user', 'comment', 'rating']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'name', 'releaseYear', 'genre', 'imageId']

class MovieSerializer(ModelSerializer):
    media = MediaSerializer()
    class Meta:
        model = Movie
        fields = '__all__'

class ShortMovieSerializer(ModelSerializer):
    media = MediaSerializer()
    class Meta:
        model = Movie
        fields = ['id', 'media', 'director']

class BookSerializer(ModelSerializer):
    media = MediaSerializer()
    class Meta:
        model = Book
        fields = '__all__'

class ShortBookSerializer(ModelSerializer):
    media = MediaSerializer()
    class Meta:
        model = Book
        fields = ['id', 'media', 'authors']

class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']

class NewUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'cityId']
    
    # Modified create method which hashes the password
    def create(self, data):
        ph = PasswordHasher(time_cost=2, memory_cost=65536, parallelism=4) # The parallelism optional argument should be set to the number of cores of the server CPU
        hashedPassword = ph.hash(data['password'])
        data['password'] = hashedPassword
        return User.objects.create(**data)

class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        # If username validation is left included it conflicts with the already existing username in the database
        extra_kwargs = {
            'username': {'validators': []},
        }