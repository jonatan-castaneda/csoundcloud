from django.shortcuts import render
import requests
import json
from .forms import AddArtistaForm, AddAlbumForm

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

def add_artista(request):
    form = AddArtistaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            data = {
                'nombre': form.cleaned_data['nombre'],
                'nacionalidad' : form.cleaned_data['nacionalidad'],
                'acerca_de': form.cleaned_data['acerca_de'],
                'tipo_artista' : form.cleaned_data['tipo_artista'],
                'genero' : form.cleaned_data['genero'],
                
            }
            r = requests.post("http://localhost:8000/api/v1/artistas/",data=data)
            print(r.status_code)
            r = requests.get("http://localhost:8000/api/v1/artistas")
            string = r.text
            json_str = json.loads(string, encoding=None) 
            return render(request, "landing/artistas.html",{
                'artistas':json_str
            })
        

    else:
        return render(request, "landing/add_artista.html", {
            'form':form
        })

def add_album(request):
    form = AddAlbumForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            data = {
                'nombre': form.cleaned_data['nombre'],
                'anio' : form.cleaned_data['anio'],
                'artista': form.cleaned_data['artista'],
                'genero' : form.cleaned_data['genero'],
                
            }
            r = requests.post("http://localhost:8000/api/v1/music/albums/",data=data)
            print(r.status_code)
            r = requests.get("http://localhost:8000/api/v1/music/albums")
            string = r.text
            json_str = json.loads(string, encoding=None) 
            return render(request, "landing/albums.html",{
                'albums':json_str
            })
        

    else:
        return render(request, "landing/add_album.html", {
            'form':form
        })