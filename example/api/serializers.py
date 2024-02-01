from rest_framework.serializers import ModelSerializer
from example.models import City, User, Movie
from argon2 import PasswordHasher

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movieId', 'mediaId', 'director']

class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ['cityId', 'name']

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