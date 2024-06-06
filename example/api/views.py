from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from example.models import *
from .serializers import *
from argon2 import PasswordHasher, exceptions
import os, uuid
from azure.storage.blob import BlobServiceClient
from django.core.paginator import Paginator
from django.db.models import Q


@api_view(['POST'])
def getStatus(request):
    try:
        # tries to find status in database, if successful returns true
        try:
            q = Status.objects.get(user=request.data['userId'], media=request.data['mediaId'])
            mediastatus = True
        except Status.DoesNotExist:
            mediastatus = False
        return Response({'status':mediastatus}, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def setStatus(request):
    try:
        # check if requested status parameter is valid
        requestedStatus = request.data['status'].capitalize()
        if requestedStatus not in ['True', 'False']:
            raise Exception
        requestedStatus = eval(requestedStatus)
        # finds status
        try:
            q = Status.objects.get(user=request.data['userId'], media=request.data['mediaId'])
            mediastatus = True
        except Status.DoesNotExist:
            mediastatus = False
        # if status doesn't match, changes it
        if mediastatus != requestedStatus:
            if mediastatus:
                q.delete()
            else:
                Status.objects.create(user_id=request.data['userId'], media_id=request.data['mediaId'])
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def createList(request):
    try:
        listArgs = {}
        listArgs['category'] = Category.objects.get(name=request.data['category'])
        listArgs['user_id'] = request.data['userId']
        listArgs['name'] = request.data['name']
        listArgs['description'] = request.data['description']
        # image handling
        blobId = None
        if len(request.FILES) > 0:
            file = request.FILES['image']
            blobId = str(uuid.uuid4())
            bsclient = BlobServiceClient.from_connection_string(os.environ.get('AZURE_STORAGE_CONNECTION_STRING'))
            blobClient = bsclient.get_blob_client(container='images', blob=blobId+".jpg")
            blobClient.upload_blob(file.read())
        listArgs['imageId'] = blobId

        newList = List.objects.create(**listArgs)
        return Response({"id":newList.id}, status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def list(request, listId):
    try:
        # add media to list
        if request.method == 'POST':
            # check if media already in list
            try:
                q = List_contains_media.objects.get(list=listId, media=request.data['mediaId'])
            except List_contains_media.DoesNotExist:
                new = List_contains_media.objects.create(list_id=listId, media_id=request.data['mediaId'])
            return Response(status=status.HTTP_200_OK)
        
        # remove media from list
        if request.method == 'DELETE':
            q = List_contains_media.objects.get(list=listId, media=request.data['mediaId'])
            q.delete()
            return Response(status=status.HTTP_200_OK)

        # get medias from list
        if request.method == 'GET':
            category = List.objects.get(pk=listId).category.name
            specMediaClass, serializer, authorField = handleMultipleCategories(category, short=True, author=True)



            # search
            searchString = request.GET.get('search', '').strip()
            medias = specMediaClass.objects.filter(media__list_contains_media__list__id=listId)
            if searchString != '':
                medias = medias.filter(Q(media__name__icontains=searchString) | Q(media__genre__icontains=searchString) | Q(**{authorField+'__icontains':searchString}))
            medias = medias.order_by('media__name')

            # pagination
            pageSize = request.GET.get('page-size', '')
            pageNumber = int(request.GET.get('page-number', '1'))
            if(pageSize != ''):
                paginator = Paginator(medias, per_page=int(pageSize))
                medias = paginator.page(pageNumber)
            
            results = serializer(medias, many=True).data
            return Response(results)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getUser(request, userId):
    try:
        results = {}
        user = User.objects.get(pk=userId)
        results['username'] = user.username
        results['city'] = CitySerializer(user.city).data
        userLists = List.objects.filter(user__id=userId)
        userLists = ListSerializer(userLists, many=True)
        results['lists'] = userLists.data
        return Response(results, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Handles POST requests to rate a media
# Requires an object with keys: 'mediaId', 'userId', 'comment', 'rating'
# If successful returns the rating id with response status 201
# In case of an error returns a response status 400
@api_view(['POST'])
def createRating(request):
    try:
        # check if rating is valid
        if(request.data['rating'] > 5 or request.data['rating'] < 1):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        newRating = Rating.objects.create(media_id=request.data['mediaId'], user_id=request.data['userId'], comment=request.data['comment'], rating=request.data['rating'])
        return Response({'id': newRating.id}, status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Takes category string (e.g. 'movie') and returns the matching model object, serializer object and author field name (e.g. Movie, MovieSerializer and 'director')
def handleMultipleCategories(category, short=False, author=False):
    if category == 'movie':
        resModel = Movie
        authorField = 'director'
        if short:
            resSerializer = ShortMovieSerializer
        else:
            resSerializer = MovieSerializer
    elif category == 'book':
        resModel = Book
        authorField = 'authors'
        if short:
            resSerializer = ShortBookSerializer
        else:
            resSerializer = BookSerializer
    if author:
        return resModel, resSerializer, authorField
    return resModel, resSerializer


@api_view(['GET'])
def singleMedia(request, category, mediaId):
    try:
        specMediaClass, serializer = handleMultipleCategories(category)

        specMedia = specMediaClass.objects.get(id=mediaId)
        results = serializer(specMedia).data
        # querying ratings
        try:
            ratings = Rating.objects.filter(media=specMedia.media.id)
            results['ratings'] = RatingSerializer(ratings, many=True).data
        except Rating.DoesNotExist:
            results['ratings'] = []
        return Response(results)
    except: 
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def media(request, category):
    try:
        specMediaClass, serializer, authorField = handleMultipleCategories(category, short=True, author=True)
        
        # get all specific medias
        if request.method == 'GET':
            # search
            searchString = request.GET.get('search', '').strip()
            if searchString == '':
                medias = specMediaClass.objects.all()
            else:
                medias = specMediaClass.objects.filter(Q(media__name__icontains=searchString) | Q(media__genre__icontains=searchString) | Q(**{authorField+'__icontains':searchString}))
            medias = medias.order_by('media__name')

            # pagination
            pageSize = request.GET.get('page-size', '')
            pageNumber = int(request.GET.get('page-number', '1'))
            if(pageSize != ''):
                paginator = Paginator(medias, per_page=int(pageSize))
                medias = paginator.page(pageNumber)
            
            results = serializer(medias, many=True).data
            return Response(results)
        # create media
        if request.method == 'POST':
            # image handling
            blobId = None
            if len(request.FILES) > 0:
                file = request.FILES['image']
                blobId = str(uuid.uuid4())
                bsclient = BlobServiceClient.from_connection_string(os.environ.get('AZURE_STORAGE_CONNECTION_STRING'))
                blobClient = bsclient.get_blob_client(container='images', blob=blobId+".jpg")
                blobClient.upload_blob(file.read())

            # separating Media and specific media arguments
            mediaParams = ['name', 'releaseYear', 'genre']
            mediaArgs = {}
            otherArgs = {}
            mediaArgs['imageId'] = blobId
            mediaArgs['category'] = Category.objects.get(name=category)
            for k, v in request.data.items():
                if k in mediaParams:
                    mediaArgs[k] = v
                else:
                    otherArgs[k] = v
            otherArgs.pop('image', None)
            newMedia = Media.objects.create(**mediaArgs)
            newSpecMedia = specMediaClass.objects.create(media=newMedia, **otherArgs)
            
            return Response({"id":newSpecMedia.id}, status=status.HTTP_201_CREATED)
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