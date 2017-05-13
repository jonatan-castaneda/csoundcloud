from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    return render(request, "landing/index.html")

def dashboard(request):
    return render(request, "landing/dashboard.html")
