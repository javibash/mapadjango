from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def mapa(request):
    return render(request, "mapa.html")

