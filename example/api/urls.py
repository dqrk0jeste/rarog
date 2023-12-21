from django.urls import path
from . import views


urlpatterns = [
    path('cities/', views.getCities),
    path('signup/', views.createUser),
    path('login/', views.login),
]