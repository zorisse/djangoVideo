from django.shortcuts import render, get_object_or_404
# import du module httpResponse
from django.http import HttpResponse

# import des models
from .models import Movie

# Create your views here.


def index(request):
    # CRUD
    movies = Movie.objects.all()
    # moviesName = [m.name for m in movies]
    # moviesNameStr = ','.join(moviesName)
    # return HttpResponse(moviesNameStr)
    return render(request, 'movies/index.html', {'movies': movies})


# create a new view fonction
#
def detail(request, movie_id):
    # CRUD
    # movie = Movie.objects.get(id=movie_id)
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
