from django.http import HttpResponse
from django.template import loader
from .models import Album
from django.shortcuts import render

def index(request):
        all_albums = Album.objects.all()
        template = loader.get_temlate('music/index.html')

        return HttpResponse('')


def detail(request, album_id):
        return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")