from django.urls import path, re_path
from . import views

categories = ['movie', 'book']
regexString = '|'.join(categories)

urlpatterns = [
    re_path(r'^user/(?P<userId>[a-zA-Z0-9-]{1,})/$', views.getUser),
    path('getstatus/', views.getStatus),
    path('setstatus/', views.setStatus),
    path('list/', views.createList),
    re_path(r'^list/(?P<listId>[a-zA-Z0-9-]{1,})/$', views.list),
    path('rate/', views.createRating),
    re_path(r'^(?P<category>('+regexString+r'))/$', views.media),
    re_path(r'^(?P<category>('+regexString+r'))/(?P<mediaId>[a-zA-Z0-9-]{1,})/$', views.singleMedia),
    path('cities/', views.getCities),
    path('signup/', views.createUser),
    path('login/', views.login),
    
]