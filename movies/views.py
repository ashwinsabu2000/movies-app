from django.shortcuts import render
from django.http import Http404
from .models import Movie


def index(request):
    newest_movies = Movie.objects.order_by('-release_date')[:15]
    context = {'newest_movies': newest_movies}
    return render(request, 'movies/index.html', context)
    
def show(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movies/show.html', {'movie': movie})