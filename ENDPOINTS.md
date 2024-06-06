# Exposed endpoints
List of endpoints exposed on https://rarog-django.vercel.app/api/


## POST /getstatus
Handles POST requests to get media status for a user.\
Requires a JSON body
```sh
{
    "mediaId": String,
    "userId": String
}
```
Returns a JSON body
```sh
{
    "status": Boolean
}
```
In case of an error returns a response status 400.

## POST /setstatus
Handles POST requests to change media status for a user.\
Requires a JSON body
```sh
{
    "mediaId": String,
    "userId": String,
    "status": Boolean
}
```
In case of an error returns a response status 400.

## POST /list
Handles multipart POST requests to create a new list for a user.\
Image file (JPEG or PNG) is optional and should be labeled 'image'.\
Required body:
```sh
{
    "userId": String,
    "category": String,
    "name": String,
    "description": String
}
```
In case of an error returns a response status 400.

## GET /list/`<id>`
Handles GET requests to get all media objects from list with `<id>` id.\
`page-number` and `page-size` are optional URL parameters for pagination.\
`search` is an optional URL parameter for search by title, genre and author.\
Returns a JSON body:\
Movies:
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
        },
        "director": String
    }
]
```
Books:
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
        },
        "authors": String
    }
]
```
In case of an error returns a response status 400.

## POST /list/`<id>`
Handles POST requests to add a media to list with `<id>` id.\
Requires a JSON body
```sh
{
    "mediaId": String,
}
```
In case of an error returns a response status 400.

## DELETE /list/`<id>`
Handles DELETE requests to remove a media from list with `<id>` id.\
Requires a JSON body
```sh
{
    "mediaId": String,
}
```
In case of an error returns a response status 400.

## GET /user/`<id>`
Handles GET requests to get details of user with `<id>` id.\
Returns a JSON body:
```sh
{
    "username": String,
    "city": {
        "id": String,
        "name": String
    },
    "lists": [
        {
            "id": String,
            "name": String,
            "category": {
                "name": String
            },
            "description": String,
            "imageId": String (or null)
        },
    ]
}
```
In case of an error returns a response status 400.

## POST /rate
Handles POST requests to rate a media.\
Requires a JSON body
```sh
{
    "mediaId": String,
    "userId": String,
    "comment": String,
    "rating": Integer
}
```
If successful returns a JSON body with response status 201.
```sh
{
    "id": String
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
Handles GET requests to get details on one media from chosen category.\
If successful returns a JSON body with response status 200.\
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
    "ratings": [
        {
            "id": String,
            "user": String,
            "comment": String,
            "rating": Integer
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
    "ratings": [
        {
            "id": String,
            "user": String,
            "comment": String,
            "rating": Integer
        }
    ]
}
```
In case of an error returns a response status 400.

## GET /`<categoryName>`
Handles GET requests to get all media objects from the `<categoryName>` category.\
`page-number` and `page-size` are optional URL parameters for pagination.\
`search` is an optional URL parameter for search by title, genre and author.\
Returns a JSON body:\
Movies:
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
        },
        "director": String
    }
]
```
Books:
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
        },
        "authors": String
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