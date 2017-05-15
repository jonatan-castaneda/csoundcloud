from django.conf.urls import url
from .views import index, dashboard, artistas, albums, canciones, guarda

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^dashboard/$', dashboard, name="dashboard"),
    url(r'^artistas/$', artistas, name="artistas"),
    url(r'^albums/$', albums, name="albums"),
    url(r'^canciones/$', canciones, name="canciones"),
    url(r'^artistas/(?P<id>[0-9]+)$', artistas, name="artistas_find"),
    url(r'^canciones/(?P<album>[0-9]+)$', canciones, name="canciones_find"),
    url(r'^albums/(?P<artista>[0-9]+)$',albums, name="albums_find"),
    url(r'^guarda/$', guarda, name="guarda"),
]
