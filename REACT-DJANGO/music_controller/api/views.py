from django.shortcuts import render
from django.http import HttpResponse # import HttpResponse to return a simple response from the view

# Create your views here.
def main(request):
    return HttpResponse("<h1>Hello, World! This is the main view of the API app. </h1>") # This view will return a simple "Hello, World!" message when accessed. You can replace this with more complex logic as needed for your API.