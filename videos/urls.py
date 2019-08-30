# module path
from django.urls import path
from . import views

# liste des routes
urlpatterns = [
    # /movies/ index
    # la racine est defini dans le projet de depart
    path('', views.index, name='index')
]
