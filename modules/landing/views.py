from django.shortcuts import render
<<<<<<< HEAD

=======
import requests
import json
>>>>>>> origin/ian
# Create your views here.
def index(request):
    return render(request, "landing/index.html")

def dashboard(request):
    return render(request, "landing/dashboard.html")

def artistas(request):
    r = requests.get("http://localhost:8000/api/v1/artistas?format=json")
    string = r.text
    json_str = json.loads(string, encoding=None)
    
    return render(request, "landing/artistas.html", {
        'artistas' : json_str,
        })
