# Exposed endpoints
List of endpoints exposed on https://rarog-django.vercel.app/api/


## POST /createcomment
Handles POST requests to create a new comment.\
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

## POST /`<categoryName>`
Handles multipart POST requests to create a new media within `<categoryName>` category.\
Image file (JPEG or PNG) is optional and should be labeled 'image'.\
Required body:\
Movies:
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
Books:
```sh
{
	"name": String,
	"releaseYear": Integer,
	"genre": String,
	"authors": String,
	"description": String
}
```
If successful returns a JSON body with response status 201.
```sh
{
	"id": String
}
```
In case of an error returns a response status 400.

## GET /`<categoryName>`/`<id>`
Handles GET requests to get details on one media from chosen category.
If successful returns a JSON body with response status 200.\
Optionally `page-number` and `page-size` can be passed as URL parameters for pagination.\
Movies:
```sh
{
    "id": String,
    "media": {
        "id": String,
        "name": String,
        "releaseYear": Integer,
        "genre": String,
        "imageId": String
    },
    "director": String,
    "cast": String,
    "length": Integer,
    "description": String,
    "screenwriters": String,
    "comments": [
        {
            "id": String,
            "user": String,
            "text": String
        }
    ]
}
```
Books:
```sh
{
    "id": String,
    "media": {
        "id": String,
        "name": String,
        "releaseYear": Integer,
        "genre": String,
        "imageId": String (or null)
    },
    "authors": String,
    "description": String,
    "comments": [
        {
            "id": String,
            "user": String,
            "text": String
        }
    ]
}
```
In case of an error returns a response status 400.

## GET /`<categoryName>`
Handles GET requests to get all media objects from the `<categoryName>` category.\
Returns a JSON body:
```sh
[
    {
        "id": String,
        "media": {
            "id": String,
            "name": String,
            "releaseYear": Integer,
            "genre": String,
            "imageId": String (or null)
        }
    }
]
```
In case of an error returns a response status 400.


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
Handles POST requests to create a new user.\
Requires a JSON body
```sh
{
	"username": String,
	"password": String,
	"email": String,
	"cityId": String
}
```
If successful returns the "userId" with response status 201.\
In case of an error returns a response status 400 and a list with field names as keys and list of errors which occured on that field as values.

## POST /login
Handles POST requests for logging in a user.\
Requires a JSON body
```sh
{
	"username": String,
	"password": String
}
```
If successful returns the "userId" with response status 200.\
In case of an error returns a response status 400 and a list with field names as keys and list of errors which occured on that field as values.