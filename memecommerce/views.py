from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Just a temporary view function for the homepage
def cow(request):
    return HttpResponse("cow go moo")
