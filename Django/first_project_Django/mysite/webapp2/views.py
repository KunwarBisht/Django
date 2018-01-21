from django.shortcuts import render

from django.http import HttpResponse

def peragraph(request):
    return HttpResponse("<h2>Hello Kunwar how are you?<h2>")
