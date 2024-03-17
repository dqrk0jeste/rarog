from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from example.models import City, User, Movie, Book, Media, Comment, Category
from .serializers import CitySerializer, NewUserSerializer, LoginSerializer, MovieSerializer, BookSerializer, CommentSerializer, MediaSerializer
from argon2 import PasswordHasher, exceptions


# Handles POST requests to create a new comment
# Requires an object with keys: 'mediaId', 'userId', 'text'
# If successful returns commentId with response status 200
# In case of an error returns a response status 400
@api_view(['POST'])
def createComment(request):
    try:
        newComment = Comment.objects.create(media_id=request.data['mediaId'], user_id=request.data['userId'], text=request.data['text'])
        return Response({'commentId': newComment.id}, status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Handles POST requests to create a new media
# Requires an object with all keys from the appropriate category
# If successful returns mediaId and specific media id with response status 200
# In case of an error returns a response status 400
@api_view(['POST'])
def createMedia(request, categoryName):
    mediaParams = ['name', 'releaseYear', 'genre']
    try:
        mediaArgs = {}
        otherArgs = {}
        mediaArgs['category'] = Category.objects.get(name=categoryName)
        for k, v in request.data.items():
            if k in mediaParams:
                mediaArgs[k] = v
            else:
                otherArgs[k] = v
        newMedia = Media.objects.create(**mediaArgs)
        if(categoryName == 'movie'):
            newMovie = Movie.objects.create(media=newMedia, **otherArgs)
        elif(categoryName == 'book'):
            newBook = Book.objects.create(media=newMedia, **otherArgs)
        
        return Response({"mediaId":newMedia.id}, status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Handles GET requests to retrieve a single media
# Returns a media objects with all keys from the appropriate category
# In case of an error returns a response status 400
@api_view(['GET'])
def getSingleMedia(request, mediaId):
    try:
        categoryName = Media.objects.get(id=mediaId).category.name
        if(categoryName == 'movie'):
            movie = Movie.objects.get(media=mediaId)
            results = MovieSerializer(movie).data
        elif(categoryName == 'book'):
            book = Book.objects.get(media=mediaId)
            results = BookSerializer(book).data

        try:
            comments = Comment.objects.filter(media=mediaId)
            results['comments'] = CommentSerializer(comments, many=True).data
        except Comment.DoesNotExist:
            results['comments'] = []
        return Response(results)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Handles GET requests to retrieve a list of all media in a certain category
# Returns a list of media objects with keys: 'mediaId', 'name', 'categoryId_id', 'releaseYear', 'genre'
# In case of an error returns a response status 400
@api_view(['GET'])
def getAllMedia(request, categoryName):
    try:
        medias = Media.objects.filter(category__name=categoryName)
        results = MediaSerializer(medias, many=True).data
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
        return Response({'userId':user.id}, status=status.HTTP_201_CREATED)
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
                return Response({'userId':user.id}, status=status.HTTP_200_OK)
            except exceptions.VerifyMismatchError:
                # Incorrect password
                return Response({'password':'Incorrect password.'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            # User doesn't exist
            return Response({'username':'This user does not exist.'}, status=status.HTTP_401_UNAUTHORIZED)
    # Login data is invalid
    return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)