# copt paste this throught urls.py of music_controller/api/urls.py

from django.urls import path
from .views import main # import the main view from the views.py file in the same directory

urlpatterns = [
    path('', main)
]