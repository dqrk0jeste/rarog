# Exposed endpoints
List of endpoints exposed on https://rarog-django.vercel.app/api/
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
