from django.conf.urls import url
from .views import index, dashboard, artistas

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^dashboard/$', dashboard, name="dashboard"),
    url(r'^artistas/$', artistas, name="artistas"),
]
