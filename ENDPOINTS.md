# Exposed endpoints
List of endpoints exposed on https://rarog-django.vercel.app/api/


## POST /createcomment
Handles POST requests to create a new comment.
Requires a JSON body
```sh
{
	"mediaId": String,
	"userId": String,
	"text": String
}
```
If successful returns a JSON body with response status 201.
```sh
{
	"commentId": String
}
```
In case of an error returns a response status 400.

## POST /createmedia/movie
Handles POST requests to create a new movie.
Requires a JSON body
```sh
{
	"name": String,
	"releaseYear": Integer,
	"genre": String,
	"director": String,
	"cast": String,
	"length": Integer,
	"description": String,
	"screenwriters": String
}
```
If successful returns a JSON body with response status 201.
```sh
{
	"mediaId": String,
	"movieId": String
}
```
In case of an error returns a response status 400.

## GET /getmedia/movie/`<mediaId>`
Handles GET requests to get details on one movie.
If successful returns a JSON body with response status 200.
```sh
[
	{
		"mediaId": String,
		"name": String,
		"releaseYear": Integer,
		"genre": String,
		"movieId": String,
		"director": String,
		"cast": String,
		"length": Integer,
		"description": String,
		"screenwriters": String,
		"comments": [
			{
				"id": String,
				"user_id": String,
				"text": String
        	}
		]
	}
]
```
In case of an error returns a response status 400.

## GET /getmedia/movie
Returns an array of movies in JSON
```sh
[
	{
		"mediaId": String,
		"name": String,
		"releaseYear": Integer,
		"genre": String
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