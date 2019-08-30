from django.shortcuts import render
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
