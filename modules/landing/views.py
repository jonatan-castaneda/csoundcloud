from django.shortcuts import render
import requests
import json
from django.http import HttpResponse
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

def guarda(request):
    #para guardar archivos con el api
    url = 'http://localhost:8000/api/v1/music/files/'
    files = {'file': open('/home/adrian/logo_unam.png', 'rb')}
    r = requests.post(url, files=files)
    print(r.text)
    
    # para hacer update a la tabla canciones con el api
    url = 'http://127.0.0.1:8000/api/v1/music/canciones/1/'
    cancion = {
        "id": 1,
        "nombre": "Cancion 1",
        "anio": 2015,
        "genero": "LA",
        "album": 1,
        "rating": "5.00",
        "url_cancion": "logo_unam.png"
    }
    r = requests.put(url,data=cancion)

    return HttpResponse("guardado")