from rest_framework.serializers import ModelSerializer
from example.models import City, User

class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class NewUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        # If email validation is left included it conflicts with the already existing email in the database
        extra_kwargs = {
            'email': {'validators': []},
        }