from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You've reached watchdawg!")
    return render(request, 'watchdawg/login.html')