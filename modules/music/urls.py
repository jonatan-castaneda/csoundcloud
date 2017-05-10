from django.conf.urls import url, include
from django.contrib import admin
from .views import ListAlbum,DetailAlbum,ListCanciones,DetailCanciones

urlpatterns = [
    url(r'^albums/$', ListAlbum.as_view() ),
    url(r'^albums/(?P<pk>[0-9]+)/$', DetailAlbum.as_view()),
    url(r'caciones/^$', ListCanciones.as_view() ),
    url(r'canciones/^(?P<pk>[0-9]+)/$', DetailCanciones.as_view())
]