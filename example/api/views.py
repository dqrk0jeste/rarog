from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from example.models import City, User, Movie, Media
from .serializers import CitySerializer, NewUserSerializer, LoginSerializer, MovieSerializer, OneMovieSerializer
from argon2 import PasswordHasher, exceptions
from django.shortcuts import get_object_or_404


#Temporary replacement for databese(movies)
movies = [
        {
        "mediaId": "d203aeb9-e4ca-431e-a391-2c030bb16804",
        "name": "The Theory of Everything",
        "releaseYear": 2014,
        "genre": "Biography/Drama/Romance",
        "movieId": "76d3b14b-dd89-4dcd-a77d-ceb7f60f64cb",
        "director": "James Marash",
        "cast": "Eddie Redmayne, Felicity Jones, Charlie Cox, David Thewlis, Simon McBurney, Emily Watson, Maxine Peake",
        "length": 123,
        "description": "Stephen Hawking gets unprecedented success in the field of physics despite being diagnosed with motor neuron disease at the age of 21. He defeats awful odds as his first wife Jane aids him loyally.",
        "screenwriters": "Anthony McCarten, Jane Hawking"
        },
        {
        "mediaId": "86925d51-3807-4fbe-9267-fb10ff039fca",
        "name": "Bride wars",
        "releaseYear": 2009,
        "genre": "Comedy/Romance",
        "movieId": "1948949a-3455-4870-8c93-b639f5c74caf",
        "director": "Gary Winick",
        "cast": "Kate Hudson, Anne Hathaway, Bryan Greenberg, Chris Pratt, Steve Howey, Candice Bergen, Kristen Johnston, Michael Arden, Victor Slezak",
        "length": 89,
        "description": "Two best friends become rivals when they schedule their respective weddings on the same day.",
        "screenwriters": "Greg DePaul, Casey Wilson	, June Diane Raphael"
        },
        {
        "mediaId": "2718f617-e06d-4ca1-b539-2acd61f12cd9",
        "name": "Oppenheimer",
        "releaseYear": 2023,
        "genre": "Biography/Drama/History",
        "movieId": "8767b2e2-73a0-4598-9e93-171285f08561",
        "director": "Christopher Nolan",
        "cast": "Cillian Murphy, 	Emily Blunt, Robert Downey Jr., Alden Ehrenreich, Scott Grimes, Jason Clarke, Kurt Koehler, Tony Goldwyn",
        "length": 180,
        "description": "The story of American scientist J. Robert Oppenheimer and his role in the development of the atomic bomb.",
        "screenwriters": "Christopher Nolan, Kai Bird, Martin Sherwin"
        },
        {
        "mediaId": "33d0c296-a1b8-4daa-880d-d3c154337752",
        "name": "Thor: Ragnarok",
        "releaseYear": 2017,
        "genre": "Action/Adventure/Comedy",
        "movieId": "0ac85360-0a65-4752-881e-f19765be8156",
        "director": "Taika Waititi",
        "cast": "Chris Hemsworth, Tom Hiddleston, Cate Blanchett, Idris Elba, Jeff Goldblum, Tessa Thompson, Karl Urban, Mark Ruffalo, Anthony Hopkins, Benedict Cumberbatch, Taika Waititi",
        "length": 130,
        "description": "Imprisoned on the planet Sakaar, Thor must race against time to return to Asgard and stop Ragnarök, the destruction of his world, at the hands of the powerful and ruthless villain Hela.",
        "screenwriters": "Eric Pearson, Craig Kyle, Christopher L. Yost"
        },
        {
        "mediaId": "6884630a-d9a7-4a93-8cef-5a689f37510f",
        "name": "Avengers: Endgame",
        "releaseYear": 2019,
        "genre": "Action/Adventure/Drama",
        "movieId": "04ca4da7-a796-4a10-8905-52f9d7a17779",
        "director": "Anthony Russo,	Joe Russo",
        "cast": "Robert Downey Jr., 	Chris Evans, Mark Ruffalo, Chris Hemsworth, Scarlett Johansson, Jeremy Renner, Don Cheadle, Paul Rudd, Benedict Cumberbatch, Chadwick Boseman, Tom Holland, Karen Gillan, Zoe Saldana, Evangeline Lilly, Elizabeth Olsen, Anthony Mackie, Sebastian Stan, Tom Hiddleston, Benedict Wong",
        "length": 181,
        "description": "After the devastating events of  Avangers: Infinity war(2018), the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe.",
        "screenwriters": "Christopher Markus, Stephen McFeely"
        },
        {
        "mediaId": "8155b00e-f351-4185-83f9-c192d7b6740b",
        "name": "Star Wars: Episode VI - Return of the Jedi",
        "releaseYear": 1983,
        "genre": "Action/Adventure/Fantasy",
        "movieId": "23d624fb-86e1-472e-8639-c43199d55ec2",
        "director": "Richard Marquand",
        "cast": "	Mark Hamill, Harrison Ford, Carrie Fisher, Billy Dee Williams, Anthony Daniels, Peter Mayhew, Sebastian Shaw, Ian McDiarmid, Frank Oz",
        "length": 131,
        "description": "After rescuing Han Solo from Jabba the Hutt, the Rebels attempt to destroy the second Death Star, while Luke struggles to help Darth Vader back from the dark side.",
        "screenwriters": "Lawrence Kasdan,	George Lucas"
        },
        {
        "mediaId": "a69ceeec-995a-4521-a51a-5be50d28a4a4",
        "name": "The Lord of the Rings: The Return of the King",
        "releaseYear": 2003,
        "genre": "Action/Adventure/Drama",
        "movieId": "ddab6633-bde5-46b4-ad94-d6e3a4706827",
        "director": "Peter Jackson",
        "cast": "	Cate Blanchett, Orlando Bloom, Billy Boyd, Bernard Hill, Ian Holm, Bruce Hopkins, Ian McKellen, Dominic Monaghan, Viggo Mortensen, John Noble, John Rhys-Davies, David Wenham, Elijah Wood",
        "length": 201,
        "description": "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",
        "screenwriters": "Fran Walsh, Philippa Boyens, Peter Jackson"
        },





        {
        "mediaId": "5359f649-031c-4d52-8da9-e54a6e4a3d6c",
        "name": "Fight Club",
        "releaseYear": 1999,
        "genre": "Thriller/Action",
        "movieId": "4da08b8d-5fb0-4ef0-8ca7-3e1b7ae0f124",
        "director": "David Fincher",
        "cast": "Brad Pitt, Edward Norton, Helena Bonham Carter, Meat Loaf, Jared Leto",
        "length": 139,
        "description": "Unhappy with his capitalistic lifestyle, a white-collared insomniac forms an underground fight club with Tyler, a careless soap salesman. Soon, their venture spirals down into something sinister.",
        "screenwriters": "Chuck Palahniuk, Jim Uhls"
        },
        {
        "mediaId": "9748d897-3040-463c-aca1-b40138d45c1d",
        "name": "Parasite",
        "releaseYear": 2019,
        "genre": "Thriller/Comedy",
        "movieId": "b419ca42-82bd-4404-b97d-02fc0d69cb2f",
        "director": "Bong Joon-ho",
        "cast": "Song Kang-ho, Lee Sun-kyun, Cho Yeo-jeong, Choi Woo-shik, Park So-dam, Jang Hye-jin",
        "length": 132,
        "description": "The struggling Kim family sees an opportunity when the son starts working for the wealthy Park family. Soon, all of them find a way to work within the same household and start living a parasitic life.",
        "screenwriters": "Bong Joon Ho, Han Jin-won"
        },
        {
        "mediaId": "4010c868-1b7a-4746-a1b7-6fc3f8b0ffb5",
        "name": "Bohemian Rhapsody",
        "releaseYear": 2018,
        "genre": "Musical/Documentary",
        "movieId": "feceaad2-8eca-4753-ab4d-97105bd39a4e",
        "director": "Bryan Singer",
        "cast": "Rami Malek, Lucy Boynton, Gwilym Lee, Ben Hardy, Joe Mazzello, Aidan Gillen, Tom Hollander, Mike Myers",
        "length": 132,
        "description": "The story of the legendary British rock band Queen and lead singer Freddie Mercury, leading up to their famous performance at Live Aid (1985).",
        "screenwriters": "Anthony McCarten, Peter Morgan"
        },
        {
        "mediaId": "e81ee8de-1469-45da-89ed-334724ce6adc",
        "name": "Variola Vera",
        "releaseYear": 1982,
        "genre": "Horror/Drama",
        "movieId": "cc94e3f5-98aa-4a22-ac38-29200958d443 ",
        "director": "Goran Markovic",
        "cast": "Rade Serbedzija, Erland Josephson, Rade Markovic",
        "length": 110,
        "description": "In 1972, a man travelling through Yugoslavia catches a disease from a shopkeeper, which is later misdiagnosed in the hospital, resulting in a massive smallpox outbreak across Belgrade.",
        "screenwriters": "Goran Markovic, Milan Nikolic"
        }
    ]



# Handles GET requests to retrieve a list of movies
# Returns a list of movies with keys: 'mediaId', 'movieId', 'name', 'director', 'genre', 'releaseYear'
# @api_view(['GET'])
# def getMovies(request):
#     queryset = Movie.objects.all()
#     serializer = MovieSerializer(queryset, many=True)
#     for movie in serializer.data:
#         media = Media.objects.get(mediaId=movie["mediaId"])
#         movie["name"] = media.name
#         movie["genre"] = media.genre
#         movie["releaseYear"] = media.releaseYear
#     return Response(serializer.data)

#Temporary version of getMovies api that works without connection to databese
#Returns a list of movies with keys: 'movieId', 'mediaId', 'director', "name", "genre", "releaseYear", "cast", "length", "description", "screenwriters"
@api_view(['GET'])
def getMovies(request):
    return Response(movies)

#Temporary version of getOneMovie api that works without connection to databese
#Returns a movie with keys: 'movieId', 'mediaId', 'director', "name", "genre", "releaseYear", "cast", "length", "description", "screenwriters"
@api_view(['GET'])
def getOneMovie(request, movieId):
    for movie in movies:
        if movie["movieId"] == movieId:
            return Response(movie)


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