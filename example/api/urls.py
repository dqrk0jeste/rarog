from django.urls import path
from . import views


urlpatterns = [
    path('movies/<str:movieId>', views.getMovie),
    path('movies/', views.getMovies),
    path('cities/', views.getCities),
    path('signup/', views.createUser),
    path('login/', views.login),
    
]