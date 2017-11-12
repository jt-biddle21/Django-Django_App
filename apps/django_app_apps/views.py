from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect


def index(request):
    response = "Hey there! Welcome to blogspot!"
    return HttpResponse(response)


def new(request):
    response = "Welcome to the create a blog page!"
    return HttpResponse(response)


def create(request):
    return redirect('/')
