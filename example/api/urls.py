from django.urls import path
from . import views


urlpatterns = [
    path('onemovie/<str:movieId>', views.getOneMovie),
    path('movies/', views.getMovies),
    path('cities/', views.getCities),
    path('signup/', views.createUser),
    path('login/', views.login),
    
]