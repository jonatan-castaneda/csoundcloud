from django.shortcuts import render
import requests
import json
# Create your views here.
def index(request):
    return render(request, "landing/index.html")

def dashboard(request):
    return render(request, "landing/dashboard.html")

def artistas(request, id=False):
    r = requests.get("http://localhost:8000/api/v1/artistas?format=json")
    string = r.text
    json_str = json.loads(string, encoding=None)
    
    return render(request, "landing/artistas.html", {
        'artistas' : json_str,
        })

def albums(request, artista=False):
    if artista:
        r = requests.get("http://localhost:8000/api/v1/music/albums?format=json&autor=%s" % (artista))
    else:
        r = requests.get("http://localhost:8000/api/v1/music/albums?format=json")
    string = r.text
    json_str = json.loads(string)

    return render(request, "landing/albums.html", {
        'albums': json_str
    })

def canciones(request, album=False):
    if album:
        r = requests.get("http://localhost:8000/api/v1/music/canciones?format=json&album=%s" % (album))
    else:
        r = requests.get("http://localhost:8000/api/v1/music/canciones?format=json")
    string = r.text
    json_str = json.loads(string)

    return render(request, "landing/canciones.html", {
        'canciones': json_str
    })
