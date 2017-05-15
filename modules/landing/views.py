from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    return render(request, "landing/index.html")

def dashboard(request):
    return render(request, "landing/dashboard.html")

def artistas(request):
    r = requests.get("http://localhost:8000/api/v1/artistas/")
    string = r.text
    json_str = json.loads(string, encoding=None)
    
    return render(request, "landing/artistas.html", {
        'artistas' : json_str,
        })
