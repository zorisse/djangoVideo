from django.contrib import admin


# Register your models here.

# 1 import the models

from .models import Genre, Movie

# customize admin


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Genre, GenreAdmin)


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('name', 'nbr_en_stock', 'prix')


admin.site.register(Movie, MovieAdmin)
