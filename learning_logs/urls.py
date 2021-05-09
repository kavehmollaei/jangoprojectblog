from os import name
from learning_logs.models import Topic
from django.contrib.admin import decorators
from django.urls import path
from . import views




app_name = "learning_logs" # name space for urls.py here 
urlpatterns= [
    path("",views.index,name="index"),
    path("topics",views.topics,name="topics"),
    path("persons",views.person,name="persons")
]


