from django.urls import path, re_path
from . import views

categories = ['movie', 'book']
regexString = '|'.join(categories)

urlpatterns = [
    path('createcomment/', views.createComment),
    re_path(r'^(?P<category>('+regexString+r'))/$', views.media),
    re_path(r'^(?P<category>('+regexString+r'))/(?P<mediaId>[a-zA-Z0-9-]{1,})/$', views.singleMedia),
    path('cities/', views.getCities),
    path('signup/', views.createUser),
    path('login/', views.login),
    
]