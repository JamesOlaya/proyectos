from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello( request ) :
    return HttpResponse("hello world!")

def about( request ):
    return HttpResponse('<h1>about us</h1>')

def product (request):
    return HttpResponse('<h1>product</h1>')