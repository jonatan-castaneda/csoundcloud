from rest_framework import serializers
from .models import Cancion,Album

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ("nombre", "anio", "rating","genero")


class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = ("nombre", "anio", "genero", "albums", "rating")