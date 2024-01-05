from django.shortcuts import render
from django.views import View
from musicians.models import Musician
from albums.models import Album

class HomeView(View):
    def get(self, request, category_slug=None):
        data = Musician.objects.all()
        albums = Album.objects.all()

        if category_slug is not None:
            album = Album.objects.get(slug=category_slug)
            data = Musician.objects.filter(album=album)

        return render(request, 'homepage.html', {'data': data, 'album': albums})
