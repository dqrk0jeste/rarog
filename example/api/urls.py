from django.urls import path
from . import views


urlpatterns = [
    path('onemovie/', views.getOneMovie),
    path('movies/', views.getMovies),
    path('cities/', views.getCities),
    path('signup/', views.createUser),
    path('login/', views.login),
    
]