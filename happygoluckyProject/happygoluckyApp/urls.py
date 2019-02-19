
from django.urls import path

from . import views

#needs to be on app url page
from django.urls import path

from . import views



#the two function being called
urlpatterns = [
    path('gogetthegood/', views.gogetthegood, name='index'),
    path("happyhappyjoyjoy/", views.happyhappyjoyjoy, name='index')
]