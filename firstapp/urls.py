from django.urls import path
from . import views 

#url pattern is a list that contains all the path function

urlpatterns = [
    path('', views.index, name = 'index'),
    path('/monday', views.monday, name = 'monday')

    
]