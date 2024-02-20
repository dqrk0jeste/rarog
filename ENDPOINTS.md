# Exposed endpoints
List of endpoints exposed on https://rarog-django.vercel.app/api/



## POST /
Handles POST requests to get details on one movie.
Requires a JSON body
```sh
{
	"movieId": String,	
}
```
If successful returns the JSON body with response status 201.
```sh
{
	"mediaId": String,
		"movieId": String,
		"name": String,
		"director": String,
		"genre": String,
		"releaseYear": Integer,
		"cast": String,
		"length": Integer,
		"description": String,
		"screenwriters": Srting
}
```


In case of an error returns a response status 400 and a list with field names as keys and list of errors which occured on that field as values.



## GET /movies
Returns an array of movies in JSON
```sh
[
	{
		"mediaId": String,
		"movieId": String,
		"name": String,
		"director": String,
		"genre": String,
		"releaseYear": Integer,
		"cast": String,
		"length": Integer,
		"description": String,
		"screenwriters": Srting
	}
]
```

## GET /cities
Returns an array of cities in JSON
```sh
[
	{
		"cityId": String,
		"name": String
	}
]
```

## POST /signup
Handles POST requests to create a new user.
Requires a JSON body
```sh
{
	"username": String,
	"password": String,
	"email": String,
	"cityId": String
}
```
If successful returns the "userId" with response status 201.
In case of an error returns a response status 400 and a list with field names as keys and list of errors which occured on that field as values.

## POST /login
Handles POST requests for logging in a user.
Requires a JSON body
```sh
{
	"username": String,
	"password": String
}
```
If successful returns the "userId" with response status 200.
In case of an error returns a response status 400 and a list with field names as keys and list of errors which occured on that field as values.