from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from example.models import City, User, Movie, Media
from .serializers import CitySerializer, NewUserSerializer, LoginSerializer, MovieSerializer, OneMovieSerializer
from argon2 import PasswordHasher, exceptions
from django.db import connection
from .util import dictfetchall

# Handles POST requests to create a new comment
# Requires an object with keys: 'mediaId', 'userId', 'text'
# If successful returns commentId with response status 200
# In case of an error returns a response status 400
@api_view(['POST'])
def createComment(request):
    # Sorting the parameters
    procedureParameters = ['mediaId', 'userId', 'text']
    procedureArguments = []
    for p in procedureParameters:
        if(p in request.data):
            procedureArguments.append(request.data[p])
        else:
            procedureArguments.append(None)
    
    # Calling the stored procedure
    try:
        with connection.cursor() as cursor:
            cursor.callproc('createComment', procedureArguments)
            results = dictfetchall(cursor)[0]   
        return Response(results, status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Handles POST requests to create a new media
# Requires an object with all keys from the appropriate category
# If successful returns mediaId and specific media id with response status 200
# In case of an error returns a response status 400
@api_view(['POST'])
def createMedia(request, categoryName):
    # Defining the procedure name and required parameters depending on the category
    if(categoryName == 'movie'):
        procedureName = 'createMovie'
        procedureParameters = ['name', 'releaseYear', 'genre', 'director', 'cast', 'length', 'description', 'screenwriters']
    
    # Sorting the parameters
    procedureArguments = []
    for p in procedureParameters:
        if(p in request.data):
            procedureArguments.append(request.data[p])
        else:
            procedureArguments.append(None)

    # Calling the stored procedure
    try:
        with connection.cursor() as cursor:
            cursor.callproc(procedureName, procedureArguments)
            results = dictfetchall(cursor)[0]
        return Response(results, status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
# Handles GET requests to retrieve a single media
# Returns a media objects with all keys from the appropriate category
# In case of an error returns a response status 400
@api_view(['GET'])
def getSingleMedia(request, categoryName, mediaId):
    # Calling the stored procedure
    try:
        with connection.cursor() as cursor:
            cursor.callproc('getSingleMedia', [categoryName, mediaId])
            results = dictfetchall(cursor)[0]
            # Append comments to the results
            cursor.callproc('getMediaComments', [mediaId])
            results['comments'] = dictfetchall(cursor)
        return Response(results)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Handles GET requests to retrieve a list of all media in a certain category
# Returns a list of media objects with keys: 'mediaId', 'name', 'categoryId_id', 'releaseYear', 'genre'
# In case of an error returns a response status 400
@api_view(['GET'])
def getAllMedia(request, categoryName):
    # Calling the stored procedure
    try:
        with connection.cursor() as cursor:
            cursor.callproc('getAllMedia', [categoryName])
            results = dictfetchall(cursor)
        return Response(results)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Handles GET requests to retrieve a list of cities
# Returns a list of cities with keys: 'cityId', 'name'
@api_view(['GET'])
def getCities(request):
    queryset = City.objects.all()
    serializer = CitySerializer(queryset, many=True)
    return Response(serializer.data)

# Handles POST requests to create a new user
# Requires an object with keys: 'username', 'password', 'email', 'cityId'
# If successful returns the userId with response status 201
# In case of an error returns a response status 400 and a list with field names as keys,
# and list of errors which occured on that field as values
@api_view(['POST'])
def createUser(request):
    serializer = NewUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # Finding the new user to return its id
        user = User.objects.get(username=serializer.data['username'])
        return Response({'userId':user.userId}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Handles POST requests for user login
# Requires an object with keys: 'username', 'password'
# If successful returns the userId with response status 200
# In case of an error returns a response status 401 and a list with field names as keys,
# and list of errors which occured on that field as values
@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        try:
            # Attempt to find a user with the provided username
            user = User.objects.get(username=serializer.data['username'])
            try:
            # Check the password 
                ph = PasswordHasher(time_cost=2, memory_cost=65536, parallelism=4) # The parallelism optional argument should be set to the number of cores of the server CPU
                ph.verify(user.password, serializer.data['password'])
                return Response({'userId':user.userId}, status=status.HTTP_200_OK)
            except exceptions.VerifyMismatchError:
                # Incorrect password
                return Response({'password':'Incorrect password.'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            # User doesn't exist
            return Response({'username':'This user does not exist.'}, status=status.HTTP_401_UNAUTHORIZED)
    # Login data is invalid
    return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)