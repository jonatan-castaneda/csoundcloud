from django.shortcuts import render
from rest_framework import generics, filters
from .models import Album, Cancion
from .serializers import AlbumSerializer,CancionSerializer
import django_filters.rest_framework

# Create your views here.

class ListAlbum(generics.ListCreateAPIView):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    #filter_backends = (filter)

class DetailAlbum(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class ListCanciones(generics.ListCreateAPIView):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer

class DetailCanciones(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer