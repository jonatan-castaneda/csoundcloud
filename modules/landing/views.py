from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    return render(request, "landing/index.html")

def dashboard(request):
    return render(request, "landing/dashboard.html")


def artistas(request):
    if request.method == 'POST':
        p = {'search':request.POST['q']}
        r = requests.get("http://localhost:8000/api/v1/artistas",params=p)
        string = r.text
        json_str = json.loads(string, encoding=None)
    else:
        r = requests.get("http://localhost:8000/api/v1/artistas")
        string = r.text
        json_str = json.loads(string, encoding=None)        

    return render(request, "landing/artistas.html", {
        'artistas' : json_str,
        })


def albums(request):
    if request.method == 'POST':
        p = {'search':request.POST['q']}
        r = requests.get("http://localhost:8000/api/v1/music/albums",params=p)
        string = r.text
        json_str = json.loads(string, encoding=None)
    else:
        r = requests.get("http://localhost:8000/api/v1/music/albums")
        string = r.text
        json_str = json.loads(string, encoding=None)        

    return render(request, "landing/albums.html", {
        'albums' : json_str,
        })

def canciones(request):
    if request.method == 'POST':
        p = {'search':request.POST['q']}
        r = requests.get("http://127.0.0.1:8000/api/v1/music/canciones/",params=p)
        string = r.text
        json_str = json.loads(string, encoding=None)
    else:
        r = requests.get("http://127.0.0.1:8000/api/v1/music/canciones/")
        string = r.text
        json_str = json.loads(string, encoding=None)        

    return render(request, "landing/canciones.html", {
        'canciones' : json_str,
        })