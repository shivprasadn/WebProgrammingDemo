from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"hello/index.html")
def shiv(request): 
    return HttpResponse("Hello, Shiv!")
def hi(request):
    return HttpResponse("Hi")
def greet(request,name):
    return render(request,"hello/greet.html",{ "name" : name.capitalize()
    })