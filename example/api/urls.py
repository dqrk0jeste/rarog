from django.urls import path
from . import views


urlpatterns = [
    path('createcomment/', views.createComment),
    path('createmedia/<str:categoryName>/', views.createMedia),
    path('getsinglemedia/<str:mediaId>/', views.getSingleMedia),
    path('getmedia/<str:categoryName>/', views.getAllMedia),
    path('cities/', views.getCities),
    path('signup/', views.createUser),
    path('login/', views.login),
    
]