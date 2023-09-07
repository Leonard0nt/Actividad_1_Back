from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display2(request):
    return HttpResponse("<h1>Hola Mundo 2!</h1>")